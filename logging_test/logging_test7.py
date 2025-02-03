import logging
from logging.handlers import TimedRotatingFileHandler

# 创建一个日志记录器
logger = logging.getLogger('timed_rotating_logger')
logger.setLevel(logging.DEBUG)

# 创建一个按时间轮转的文件处理器，每天轮转一次，保留 7 个备份文件
handler = TimedRotatingFileHandler('logging_test7.log', when='midnight', interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(handler)

# 记录日志
logger.debug('这是一条按时间轮转的日志')
