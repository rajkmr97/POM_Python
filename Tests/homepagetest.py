from selenium import  webdriver
import unittest
from POMTest.Pages.homepage import HomePage
import HtmlTestRunner
class HomePageTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path='D:/Downloads/chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
    def test_home_valid(self):
        driver = self.driver
        self.driver.get('https://www.sathya.in/')
        home = HomePage(driver)
        home.click_audio()
        home.click_home_theatre()
        home.click_product()
        home.click_add_cart()
        home.click_checkout_btn()
        home.click_checkout_guest()
        home.click_billing_address()
        home.click_ship_address()
        home.click_next_button1()
        home.click_next_button2()
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/RAJKUMAR/PycharmProjects/selenium/POMTest/Reports'))

#if __name__ == '__main__':
#    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/RAJKUMAR/PycharmProjects/selenium/POMTest/Reports'))

