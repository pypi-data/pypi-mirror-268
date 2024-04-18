import logging

# ANSI escape codes for coloring
class LogColors:
    RESET = "\033[0m"
    DEBUG = "\033[34m"  # Blue
    INFO = "\033[32m"   # Green
    WARNING = "\033[33m" # Yellow
    ERROR = "\033[31m"   # Red
    CRITICAL = "\033[35m" # Magenta

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (" \
             "%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: LogColors.DEBUG + format + LogColors.RESET,
        logging.INFO: LogColors.INFO + format + LogColors.RESET,
        logging.WARNING: LogColors.WARNING + format + LogColors.RESET,
        logging.ERROR: LogColors.ERROR + format + LogColors.RESET,
        logging.CRITICAL: LogColors.CRITICAL + format + LogColors.RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%Y-%m-%d %H:%M:%S")
        return formatter.format(record)

def get_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)

    # Set the log level
    logger.setLevel(logging.DEBUG)  # Set to the lowest level to capture all messages

    # Create handlers
    c_handler = logging.StreamHandler()
    c_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = CustomFormatter()
    c_handler.setFormatter(c_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)

    return logger

# Define the global logger variable
logger = get_logger("nstreamai")

# Example usage:
if __name__ == "__main__":
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')
