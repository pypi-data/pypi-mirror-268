import logging


class Default:
    IMPLICITLY_WAIT = 5
    TIMEOUT = 5
    INTERVAL = 0.5
    ACTION_WAIT = 0.5
    REFRESH_WAIT = 2


class LogConfig:
    # STREAM输出相关配置
    STREAM = False
    STREAM_LEVEL = logging.INFO
    STREAM_FORMAT = ''

    # Log文件相关配置
    LOG_FILE = ''
    LOG_FILE_LEVEL = logging.INFO
    LOG_FILE_FORMAT = ''

    SAVE_ERROR = True
