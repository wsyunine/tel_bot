import logging

# 配置日志记录级别
logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

# 只有 WARNING 及以上级别的日志会被记录
logging.debug('这条信息不会被记录')
logging.warning('这条信息会被记录')
