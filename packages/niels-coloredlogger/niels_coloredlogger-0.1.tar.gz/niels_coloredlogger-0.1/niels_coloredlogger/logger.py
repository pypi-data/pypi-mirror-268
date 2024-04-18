import logging
import os
import coloredlogs

LOGGING_FILE = "logs/log.log"

coloredlogs.DEFAULT_LEVEL_STYLES = {
    'debug': {'color': 'green'},
    'info': {'color': 'cyan'},
    'warning': {'color': 'yellow'},
    'error': {'color': 'red'},
    'critical': {'color': 'red', 'bold': True},
}

coloredlogs.DEFAULT_FIELD_STYLES = {
    'asctime': {'color': 'green'},
    'hostname': {'color': 'magenta'},
    'levelname': {'color': 'magenta', 'bold': True},
    'name': {'color': 'magenta'},
    'programname': {'color': 'cyan'},
    'username': {'color': 'yellow'}
}

logger = logging.getLogger('niels_coloredlogger')
coloredlogs.install(level='DEBUG', logger=logger,
                    fmt='[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(module)s:%(funcName)-16s] %(message)s',
                    datefmt='%d.%m.%Y %H:%M:%S'
                    )

os.makedirs(os.path.dirname(LOGGING_FILE), exist_ok=True)
__f_handler = logging.FileHandler(LOGGING_FILE, mode='a')
__f_formatter = logging.Formatter('[%(asctime)s] [%(levelname)-8s] [%(filename)s:%(module)s:%(funcName)-16s] %(message)s',
                                  datefmt='%d.%m.%Y %H:%M:%S')
__f_handler.setLevel(logging.DEBUG)
__f_handler.setFormatter(__f_formatter)
logger.addHandler(__f_handler)


def print_all_loggers():
    loggers = [logging.getLogger(name) for name in logging.Logger.manager.loggerDict]
    for logger in loggers:
        print(f'Logger: {logger.name}, Level: {logging.getLevelName(logger.level)}')
