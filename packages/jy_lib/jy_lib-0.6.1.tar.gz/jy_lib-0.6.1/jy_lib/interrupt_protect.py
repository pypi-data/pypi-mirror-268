# -*- coding: utf-8 -*-
import signal
from loguru import logger
from types import FrameType


class KeyboardInterruptProtect:
    """
    防止代码段被Ctrl+C终止
    with KeyboardInterruptProtect():
        do()
    """
    @classmethod
    def signal_handler(cls, signum: int, frame: FrameType | None):
        logger.warning(f'Ignore KeyboardInterrupt')

    def __enter__(self):
        signal.signal(signal.SIGINT, self.signal_handler)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 重置signal处理函数为默认行为
        signal.signal(signal.SIGINT, signal.SIG_DFL)
