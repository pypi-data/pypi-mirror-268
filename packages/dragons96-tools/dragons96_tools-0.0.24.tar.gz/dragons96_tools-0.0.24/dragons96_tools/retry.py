import time
from loguru import logger

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class Retry:
    """
    重试工具
    """

    def __init__(self, max_attempts=3, delay=1,
                 log_enable: bool = True,
                 ever_fail_level: Literal['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR'] = 'WARNING',
                 fail_level: Literal['TRACE', 'DEBUG', 'INFO', 'WARNING', 'ERROR'] = 'ERROR'):
        """
        初始化重试工具
        Args:
            max_attempts (int): 最大重试次数，默认为 3 次。
            delay (float): 重试之间的延迟时间，单位为秒，默认为 1 秒。
            log_enable: 是否记录日志
            ever_fail_level: 每次失败记录的日志级别
            fail_level: 全部失败记录的日志级别
        """
        self._max_attempts = max_attempts
        self._delay = delay
        self._log_enable = log_enable
        self._ever_fail_level = ever_fail_level
        self._fail_level = fail_level

    def do(self, func, *args, **kwargs):
        """
        重试函数，重复执行指定的函数，直到达到最大重试次数或者函数执行成功为止。
        Args:
            func: 要执行的函数。
            args: 执行函数的参数
            kwargs: 执行函数的参数
        Returns:
            函数执行成功时返回函数的返回值，否则返回 None。
        """
        for attempt in range(1, self._max_attempts + 1):
            try:
                result = func(*args, **kwargs)
                return result  # 函数执行成功，直接返回结果
            except Exception as e:
                if attempt < self._max_attempts:
                    if self._log_enable:
                        logger.log(self._ever_fail_level,
                                   "函数[{}]第[{}]次执行失败, 失败原因: {}, 等待[{}]秒后将进行重试, 函数参数args: {}, kwargs: {}",
                                   func.__name__, attempt, e, self._delay, args, kwargs)
                    time.sleep(self._delay)
                else:
                    if self._log_enable:
                        logger.log(self._fail_level,
                                   '函数[{}]重试[{}]次仍然失败, 抛出异常: {}, 函数参数args: {}, kwargs: {}',
                                   func.__name__, self._max_attempts, e, args, kwargs)
                    raise e
