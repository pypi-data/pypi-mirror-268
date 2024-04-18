# -*- coding: utf-8 -*-
import clickhouse_driver
import io
import os
import polars as pl
import requests
import time
import urllib.parse
import zstandard
from typing import Dict
from loguru import logger
from jy_lib.compressor import ZstdStreamCompressor
from jy_lib.interrupt_protect import KeyboardInterruptProtect


class ClickHouse:

    def __init__(self, url: str, http_port: int = 8123):
        self.client = clickhouse_driver.Client.from_url(url=url)
        self.http_port: int = http_port
        sp = urllib.parse.urlsplit(url)
        self.database_name: str = os.path.basename(sp.path)
        assert not sp.path or sp.path == f'/{self.database_name}'
        self.url_http: str = f'http://{sp.hostname}:{http_port}'
        self.credential: Dict = {
            'user': sp.username,
            'password': sp.password,
        }
        self.execute = self.client.execute

    def bulk_insert(self, table_name: str, df: pl.DataFrame):
        columns: str = ', '.join([f'`{column}`' for column in df.columns])
        sql: str = f'INSERT INTO `{self.database_name}`.`{table_name}`({columns}) VALUES'
        with KeyboardInterruptProtect():
            logger.debug(f'[{self.database_name}.{table_name}]准备插入{df.height:12,d}条数据')
            t1: float = time.time()
            self.client.execute(query=sql, params=df.to_dicts())
            t2: float = time.time()
            logger.success(f'[{self.database_name}.{table_name}]成功插入{df.height:12,d}条数据 耗时{t2 - t1:0.0f}秒')

    def import_csv(self, table_name: str, csv: str, height: int = None):
        sql: str = f'INSERT INTO `{self.database_name}`.`{table_name}` FORMAT CSVWithNames'
        params: Dict = {
            'query': sql,
            **self.credential,
            'enable_http_compression': 1,
        }
        t1: float = time.time()
        if height is None:
            height: int = -1
            sio = io.StringIO(csv)
            while sio.readline():
                height += 1
        if not csv:
            logger.warning(f'{sql}: empty csv')
            return
        assert height >= 0
        csv: bytes = csv.encode('utf-8')
        with ZstdStreamCompressor(size=len(csv), level=zstandard.STRATEGY_FAST) as sc:
            sc.update(data=csv)
            stream: io.BytesIO = sc.stream
        with KeyboardInterruptProtect():
            logger.debug(f'[{self.database_name}.{table_name}]准备插入{height:12,d}条数据')
            r = requests.post(
                url=self.url_http,
                params=params,
                data=stream.getvalue(),
                headers={
                    'Content-Encoding': 'zstd',
                    'Accept-Encoding': 'zstd',
                },
            )
            t2: float = time.time()
        assert r.status_code == 200, f'[{r.status_code}]{r.text}'
        if r.text:
            logger.info(r.text)
        logger.success(f'[{self.database_name}.{table_name}]成功插入{height:12,d}条数据 耗时{t2 - t1:0.0f}秒')

    def import_df(self, table_name: str, df: pl.DataFrame, datetime_format='%Y-%m-%d %H:%M:%S%.f'):
        assert self.database_name
        return self.import_csv(
            table_name=table_name,
            csv=df.write_csv(include_header=True, datetime_format=datetime_format),
            height=df.height
        )
