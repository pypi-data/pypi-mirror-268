from dragons96_tools.retry import Retry
from loguru import logger

cnt = 0


def fail3(a: int, b: int):
    logger.info('请求参数a: {}, b: {}', a, b)
    global cnt
    if cnt < 3:
        cnt += 1
        raise Exception('异常')
    logger.info('cnt: {}', cnt)
    return cnt


def test_retry():
    _retry = Retry(max_attempts=10,  # 最大重试次数
                   delay=1,  # 每次重试的等待间隔, 单位秒
                   log_enable=True,  # 是否打印日志
                   ever_fail_level='WARNING',  # 每次任务失败记录的日志级别(未达到重试上限),
                   fail_level='ERROR',  # 任务重试达到失败上限的日志级别
                   )
    logger.info(_retry.do(fail3, 1, b=5))
