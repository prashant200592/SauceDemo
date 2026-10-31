import configparser
import os

config = configparser.RawConfigParser()
config.read(os.path.abspath(os.curdir+"\\configurations\\"+"config.ini"))

class ReadConfig:

    @staticmethod
    def get_url():
        return config.get('commonInfo', 'baseURL')

    @staticmethod
    def get_username():
        return config.get('commonInfo','username')

    @staticmethod
    def get_password():
        return config.get('commonInfo','password')

