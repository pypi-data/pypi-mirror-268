from loguru import logger as log
from dragons96_tools.logger import setup as stp

stp('test_logger.log')


@log.catch
def error_fun():
    return 1 / 0


def test_log_catch():
    f = error_fun()
    print(f)

