import allure
from Utility.app_maneger import AbstractDriver
from Utility.fls_page_objects.login_page import LoginPage
from Utility.generic_function import GenericFunctions
from selenium import webdriver as driver


class HomePage:

    def __init__(self):
        self.driver = AbstractDriver.get_instance_driver()
        self.gf = GenericFunctions()

    def breadcumbs_parent_elment(self):
        return self.gf.find_element(css=".bread-crumb")

    def username_arrow(self):
        return self.gf.find_element(css=".dropdown-toggle i")

    def logout_btn(self):
        return self.gf.find_element(css="#g-account-menu li a")

    def create_group(self):
        return self.gf.find_element(css=".buttonCustom.float-right")

    def box_element(self):
        return self.gf.find_elements(css=".box-body")

    @allure.step
    def validate_homepage(self):
        if self.gf.wait_for_element(self.create_group()):
            return True
        else:
            return False

    @allure.step
    def click_logout(self):
        self.gf.js_click(self.username_arrow())
        self.gf.wait_for_element(self.logout_btn())
        self.gf.js_click(self.logout_btn())
        return LoginPage()

    @allure.step
    def click_on_creategroup(self):
        from Utility.fls_page_objects.create_group import CreateGroup
        self.gf.js_click(self.create_group())
        return CreateGroup()

    @allure.step
    def click_on_edit_icon(self, group_name):
        from Utility.fls_page_objects.create_group import CreateGroup
        if(self.gf.wait_for_element(self.gf.find_element(xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+group_name+"']"))):
            self.gf.js_click_with_focus(self.gf.find_element(
                xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+group_name+"']/../..//following-sibling::div//i[@title='Edit']"))
            return CreateGroup()
        else:
            print("element not found")

    @allure.step
    def delete_group(self, group_name):
        if(self.gf.wait_for_element(self.gf.find_element(xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+group_name+"']"))):
            self.gf.js_click_with_focus(self.gf.find_element(
                xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+group_name+"']/../..//following-sibling::div//i[@title='Delete']"))
            self.gf.wait_for_element(
                self.gf.find_element(css=".p-toast-detail"))
            return True
        else:
            return False

    @allure.step
    def get_group_description(self, groupname):
        return self.gf.find_element(
            xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+groupname+"']/../../..//following-sibling::div[contains(@class,'box-desc-innr')]").text

    @allure.step
    def click_on_define_sceanrio(self, groupname):
        from Utility.fls_page_objects.createnewsceanrio import CreateNewSceanrio
        self.gf.js_click_with_focus(self.gf.find_element(
            xpath="//div[contains(@class,'text-break')]/h3/a[text()= '"+groupname+"']/../../..//following-sibling::div[contains(@class,'access-shared-with')]//button"))
        return CreateNewSceanrio()
