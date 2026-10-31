import pytest
from pageObjects.loginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

class Test_Login:

    #baseURL = "https://www.saucedemo.com/"
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info("********* Verifying Login Test **********")
        self.driver = setup

        self.logger.info("********* Launching application ********")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # Creating login page object
        self.lpo = LoginPage(self.driver)

        self.logger.info("********* Entering credentials **********")
        self.lpo.enter_username(self.username)
        self.lpo.enter_password(self.password)
        self.lpo.click_login()
        self.actual_title = self.driver.title
        self.expected_title = "Swag Labs"

        self.logger.info("********* Verifying login action **********")
        if self.actual_title == self.expected_title:
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir+"\\screenshots\\"+"test_login.png"))
            self.driver.close()
            assert False

