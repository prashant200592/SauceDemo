import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.productsPage import ProductPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time

class Test_AddToCart:
    baseURL = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_add_to_cart(self,setup):
        self.logger.info("*** Testing add_to_cart ***")
        self.driver = setup

        self.logger.info("*** Launching application")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lpo = LoginPage(self.driver)

        self.logger.info("*** Entering login credentials ***")
        self.lpo.enter_username(self.username)
        self.lpo.enter_password(self.password)
        self.lpo.click_login()

        self.ppo = ProductPage(self.driver)
        self.ppo.add_backpack_to_cart()

        time.sleep(3)
        self.driver.close()