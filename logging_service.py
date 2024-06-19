import time
import logging.handlers

logger = logging.getLogger('my_service')
logger.setLevel(logging.INFO)
syslog_handler = logging.handlers.SysLogHandler(address='/dev/log')
logger.addHandler(syslog_handler)


def run_service():
    while True:
        logger.info("Привет из моего сервиса!")
        time.sleep(10)


if __name__ == "__main__":
    run_service()
