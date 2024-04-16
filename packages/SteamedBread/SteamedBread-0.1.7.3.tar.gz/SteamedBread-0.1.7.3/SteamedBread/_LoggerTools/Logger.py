"""
@Author: 馒头 (chocolate)
@Email: neihanshenshou@163.com
@File: Logger.py
@Time: 2023/12/9 18:00
"""

import logging
import sys
from typing import Callable

from colorama import Fore, Style

_logger = logging.getLogger(__name__)


class _Style:
    _GREEN = Fore.GREEN
    _BLACK = Fore.BLACK
    _RED = Fore.RED
    _ORIGIN = Style.RESET_ALL
    _BOLD = Style.BRIGHT

    stream_format = (
        f'{_ORIGIN}{_GREEN}%(asctime)s '
        f'{_ORIGIN}{_BOLD}| %(filename)s'
        f'{_BLACK}{_BOLD} | %(lineno)s | %(levelname)s {_BOLD}| '
        f'{_BOLD}%(message)s {_ORIGIN}')

    stream_level = 'DEBUG'
    file_format = '%(asctime)s - %(filename)s - %(lineno)s - %(levelname)s - %(message)s'
    file_level = 'DEBUG'

    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

    RESET_SEQ = "\033[0m"
    COLOR_SEQ = "\033[1;%dm"
    BOLD_SEQ = "\033[1m"

    COLORS = {
        'WARNING': YELLOW,
        'INFO': CYAN,
        'DEBUG': BLUE,
        'CRITICAL': MAGENTA,
        'ERROR': RED
    }


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        level_name = record.levelname
        if self.use_color and level_name in _Style.COLORS:
            level_name_color = _Style.COLOR_SEQ % (30 + _Style.COLORS[level_name]) + level_name + _Style.RESET_SEQ
            record.levelname = level_name_color

        # 移除 ANSI 转义序列
        message = logging.Formatter.format(self, record)
        record.levelname = level_name

        return message


class ColoredLogger(logging.Logger):

    def __init__(self, name):
        logging.Logger.__init__(self, name, logging.DEBUG)
        color_formatter = ColoredFormatter(_Style.stream_format)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


def _set_filename(filename=None, level="DEBUG") -> None:
    """
    设置日志存储目录
    :param filename: 日志存储目录
    :return: None
    """
    # 文件日志中打印 debug 级别的日志
    file_handler = logging.FileHandler(filename=filename)
    file_handler.setLevel(level=level or _Style.file_level)
    file_handler.setFormatter(fmt=logging.Formatter(fmt=_Style.file_format))
    # 拒绝添加重复句柄
    _logger.addHandler(hdlr=file_handler)


def _stream_setting():
    _logger.setLevel(logging.INFO)
    # 终端只打印 info 级别的日志
    __stream_handler = logging.StreamHandler(stream=sys.stdout)
    __stream_handler.setLevel(level=_Style.stream_level)

    color_formatter = ColoredFormatter(_Style.stream_format)
    __stream_handler.setFormatter(fmt=color_formatter)

    # 拒绝添加重复句柄
    _logger.addHandler(hdlr=__stream_handler)


class Logger:
    _stream_setting()
    _logger.setFilename = _set_filename

    def __init__(self):
        self.setFilename: Callable[..., None] = self.__set_filename
        self.setLevel: Callable[..., None] = self.__set_stream_level

    @classmethod
    def __set_stream_level(cls, level: str):
        logging.StreamHandler().setLevel(level=level)

    @classmethod
    def __set_filename(cls, filename: str, level="DEBUG"):
        _set_filename(filename=filename, level=level)

    @staticmethod
    def debug(msg: str, *args, **kwargs):
        _logger.debug(msg=msg, *args, **kwargs)

    @staticmethod
    def info(msg: str, *args, **kwargs):
        _logger.info(msg=msg, *args, **kwargs)

    @staticmethod
    def warning(msg: str, *args, **kwargs):
        _logger.warning(msg=msg, *args, **kwargs)

    @staticmethod
    def error(msg: str, *args, **kwargs):
        _logger.error(msg=msg, *args, **kwargs)

    @staticmethod
    def critical(msg: str, *args, **kwargs):
        _logger.critical(msg=msg, *args, **kwargs)


logger: Logger = _logger
