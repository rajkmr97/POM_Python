from selenium import  webdriver
import time
import unittest
from POMTest.Pages.LoginPage import LoginPage
import HtmlTestRunner
class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_login_valid(self):
        driver = self.driver
        self.driver.get('https://www.sathya.in/')
        login=LoginPage(driver)
        login.click_login()
        login.enter_username("vinodh682@gmail.com")
        login.enter_password("vinodeepa")
        login.click_btn()
        login.click_login_btn()
        login.click_logout_btn()
        time.sleep(3)
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/RAJKUMAR/PycharmProjects/selenium/POMTest/Reports'))






