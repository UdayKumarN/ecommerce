import configparser

config=configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:
    @staticmethod # to Static method used to call directly without creating object
    def getApplicationUrl():
        url=config.get('common info','baseUrl')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('common info', 'password')
        return password

