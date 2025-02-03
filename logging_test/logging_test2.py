import logging

# 配置日志记录到文件
logging.basicConfig(filename='logging_test2.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# 记录日志
logging.info('这条信息会被记录到文件中')
