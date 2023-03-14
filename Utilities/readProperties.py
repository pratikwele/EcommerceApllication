import configparser
config=configparser.RawConfigParser() # method  RawConfigParser
config.read(".\\confuguration\\config.ini") # object config

class ReadConfig:

    @staticmethod
    def getApplicationUrl():
         url=config.get('common info','baseurl')
         return url
    @staticmethod
    def getUserEmail():
        username= config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password= config.get('common info','password')
        return password
