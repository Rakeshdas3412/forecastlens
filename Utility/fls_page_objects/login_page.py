import allure
from Utility.app_maneger import AbstractDriver
from Utility.generic_function import GenericFunctions


class LoginPage:

    def __init__(self):
        self.driver = AbstractDriver.get_instance_driver()
        self.gf = GenericFunctions()

    def username_textbox(self):
        return self.gf.find_element(name="username")

    def set_username(self, email):
        self.gf.send_keys(self.username_textbox(), email)

    def password_textbox(self):
        return self.gf.find_element(name="password")

    def set_password(self, password):
        self.password_textbox().send_keys(password)

    def login_btn(self):
        return self.gf.find_element(css="button[type='submit']")

    def click_login_btn(self):
        self.gf.js_click(self.login_btn())

    @allure.step
    def verify_loginpage(self):
        if self.gf.wait_for_element(self.login_btn()) == True:
            return True
        else:
            return False

    @allure.step
    def login_as_externalUser(self, uname, password):
        from Utility.fls_page_objects.home_page import HomePage
        if self.gf.wait_for_element(self.login_btn()) != True:
            self.driver.refresh()
            self.set_username(uname)
            self.set_password(password)
            self.click_login_btn()
        else:
            self.set_username(uname)
            self.set_password(password)
            self.click_login_btn()
        return HomePage()
