import logging

# 创建一个自定义的日志记录器
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)

# 创建一个文件处理器并设置级别
file_handler = logging.FileHandler('logging_test3.log')
file_handler.setLevel(logging.DEBUG)

# 创建一个控制台处理器并设置级别
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# 将处理器添加到日志记录器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 记录日志
logger.debug('这是一个调试信息')
logger.error('这是一个错误信息')
