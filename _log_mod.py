import logging
from colorama import init, Fore

# 初始化 colorama
init()

# 创建一个日志器对象
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设置日志级别





# 创建一个流处理器，并设置日志格式
stream_handler = logging.StreamHandler()

# 使用不同颜色来表示不同的日志级别
class ColoredFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.MAGENTA
    }

    def format(self, record):
        color = self.COLORS.get(record.levelno, Fore.WHITE)
        formatter = logging.Formatter(color + '%(asctime)s - %(levelname)s - %(message)s' + Fore.RESET)
        return formatter.format(record)

# 设置日志格式
formatter = ColoredFormatter()
stream_handler.setFormatter(formatter)

# 将处理器添加到日志器中
logger.addHandler(stream_handler)







