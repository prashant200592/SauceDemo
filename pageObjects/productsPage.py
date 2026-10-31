from selenium.webdriver.common.by import By

class ProductPage:
    # Locators
    button_backpack_addtocart_id = "add-to-cart-sauce-labs-backpack"


    # Constructor
    def __init__(self,driver):
        self.driver = driver

    # Action methods
    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, self.button_backpack_addtocart_id).click()

