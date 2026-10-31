import logging
import os

class LogGen:
    @staticmethod
    def loggen():
        # Ensure logs folder exists
        log_folder =os.path.join(os.path.abspath(os.curdir),'logs')
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # Full log file path
        log_file = os.path.join(log_folder,'automation.log')

        # Create logger
        logger = logging.getLogger("automation")
        logger.setLevel(logging.DEBUG)

        # Stop pytest from blocking debug logs
        logger.propagate = True

        # Avoid adding multiple handlers during PyTest runs.
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%d-%b-%y %H:%M:%S'
            )

            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        return logger
