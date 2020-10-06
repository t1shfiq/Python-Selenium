from selenium import webdriver
import time
#Python's in-buiilt testing module
import unittest

class LoginTest(unittest.TestCase):

    ## annotation for using class functions
    @classmethod
    ## setUpClass will run only once before all the test methods
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    ## test for a valid log in
    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        self.driver.find_element_by_id("btnLogin").click()
        self.driver.find_element_by_id("welcome").click()
        self.driver.find_element_by_link_text("Logout").click()
        time.sleep(5)

    @classmethod
    ## teardownclass will run after all the tests are completed
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")