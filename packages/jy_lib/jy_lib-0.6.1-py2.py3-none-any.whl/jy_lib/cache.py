# -*- coding: utf-8 -*-
import lz4.frame
import math
import pickle
import re
import sqlite3
import time
from typing import Any, Set, List


class Cache:
    """持久化TTL缓存"""

    def __init__(self, path: str):
        self.path: str = path
        self.conn = sqlite3.connect(self.path)
        self.datasets: Set[str] = self.get_tables()

    def get_tables(self) -> Set[str]:
        cursor = self.conn.cursor()
        r = cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return {row[0] for row in r.fetchall()}

    def create_table(self, dataset: str) -> None:
        assert not re.findall(r'\s', dataset)
        self.conn.execute(f"""CREATE TABLE IF NOT EXISTS `{dataset}` (
            `key` TEXT PRIMARY KEY NOT NULL,
            `value` BLOB NOT NULL,
            `expired_at` REAL NOT NULL
        )""")
        self.conn.execute(f"""CREATE INDEX IF NOT EXISTS expired_at ON `{dataset}` (`expired_at`)""")
        self.conn.commit()

    def set(self, dataset: str, key: str, value: Any, expire: float = math.inf) -> None:
        if dataset not in self.datasets:
            self.create_table(dataset=dataset)
            self.datasets.clear()
            self.datasets.update(self.get_tables())
        payload: bytes = lz4.frame.compress(pickle.dumps(value))
        sql: str = f"""REPLACE INTO `{dataset}` (`key`, `value`, `expired_at`) VALUES(?,?,?)"""
        self.conn.execute(sql, (key, payload, time.time() + expire))
        self.conn.commit()

    def delete(self, dataset: str, key: str) -> None:
        if dataset in self.datasets:
            sql: str = f"""DELETE FROM `{dataset}` WHERE `key`=?"""
            self.conn.execute(sql, (key, ))
            self.conn.commit()

    def get(self, dataset: str, key: str) -> Any | None:
        if dataset in self.datasets:
            cursor = self.conn.cursor()
            sql: str = f"""SELECT `value`, `expired_at` FROM `{dataset}` WHERE `key`=?"""
            r = cursor.execute(sql, (key, ))
            r = r.fetchone()
            if r is None:
                return r
            else:
                value, expired_at = r
                if expired_at > time.time():
                    return pickle.loads(lz4.frame.decompress(value))
                else:
                    self.delete(dataset=dataset, key=key)
                    return None

    def keys(self, dataset: str) -> List[str] | None:
        if dataset in self.datasets:
            cursor = self.conn.cursor()
            sql: str = f"""SELECT `key` FROM `{dataset}` WHERE `expired_at`>?"""
            r = cursor.execute(sql, (time.time(), ))
            return [r[0] for r in r.fetchall()]

    def close(self):
        self.conn.commit()
        self.conn.close()
