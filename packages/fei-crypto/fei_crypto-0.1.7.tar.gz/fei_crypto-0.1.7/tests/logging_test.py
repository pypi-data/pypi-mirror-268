import logging
from rich.logging import RichHandler
if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )

    logging.debug('debug 信息')
    logging.warning('warning 输出,默认级别是warning')
    logging.info('info 信息')
