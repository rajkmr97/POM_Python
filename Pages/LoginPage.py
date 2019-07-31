from POMTest.Locators.locators import Locators
class LoginPage():
    def __init__(self, driver):
        self.driver=driver
        self.login_button=Locators.login_button
        self.username_textbox=Locators.username_textbox
        self.password_textbox=Locators.password_textbox
        self.login_btn=Locators.login_btn
        self.user=Locators.user
        self.logout_btn=Locators.logout_btn

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button).click()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox).clear()
        self.driver.find_element_by_xpath(self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox).clear()
        self.driver.find_element_by_xpath(self.password_textbox).send_keys(password)

    def click_btn(self):
        self.driver.find_element_by_xpath(self.login_btn).click()

    def click_login_btn(self):
        self.driver.find_element_by_xpath(self.user).click()

    def click_logout_btn(self):
        self.driver.find_element_by_xpath(self.logout_btn).click()




