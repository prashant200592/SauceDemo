from selenium.webdriver.common.by import By

class LoginPage:
    # Locators
    txtbox_username_id = "user-name"
    txtbox_password_id = "password"
    button_login_id = "login-button"

    # Constructor
    def __init__(self,driver):
        self.driver = driver

    # Action Methods
    def enter_username(self,username):
        self.driver.find_element(By.ID, self.txtbox_username_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.txtbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.button_login_id).click()

    