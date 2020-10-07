from Python-Selenium.PageObjectModel.Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

        #objects
        self.username_testbox_id = Locators.username_textbox_id
        self.password_textbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    #all actions to be performed on the objects

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click(0)