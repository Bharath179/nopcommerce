import configparser


config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        useremail = config.get('common info', 'user_email')
        return useremail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password

    @staticmethod
    def getUrl():
        url=config.get('common data','baseurl')
        return url

    @staticmethod
    def getUserName():
        username=config.get('common data','username')
        return username

    @staticmethod
    def getPasswordfield():
        password=config.get('common data','password')
        return password