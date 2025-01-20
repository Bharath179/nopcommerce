import logging

class Log_Maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\nopcommerce.log",format='%(asctime)s [%(levelname)s] [%(module)s] %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',force=True)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger