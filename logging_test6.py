import logging
from logging.handlers import RotatingFileHandler

# 创建一个日志记录器
logger = logging.getLogger('rotating_logger')
logger.setLevel(logging.DEBUG)

# 创建一个轮转文件处理器，最大文件大小为 1MB，最多保留 3 个备份文件
handler = RotatingFileHandler('logging_test6.log', maxBytes=1*1024*1024, backupCount=3)
handler.setLevel(logging.DEBUG)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(handler)

# 记录日志
for i in range(10000):
    logger.debug(f'这是第 {i} 条日志')
