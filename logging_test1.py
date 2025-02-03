import logging

# 配置日志记录级别和格式
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 记录不同级别的日志
logging.debug('这是一个调试信息')
logging.info('这是一个普通信息')
logging.warning('这是一个警告信息')
logging.error('这是一个错误信息')
logging.critical('这是一个严重错误信息')
