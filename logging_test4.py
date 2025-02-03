import logging

# 配置日志记录
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    1 / 0
except Exception as e:
    logging.error('发生了一个异常', exc_info=True)
