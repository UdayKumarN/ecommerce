import logging


class LogGen():

    #@staticmethod  # to Static method used to call directly without creating object
    def loggen():
        logging.basicConfig(filename="Automation.log", format='%(asctime)s:%(levelname)s:%(message)s')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        print("logger started")
        return logger