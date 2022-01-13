from Utility.app_maneger import AbstractDriver, GenericFunctions
import allure
import time


class CreateGroup:

    def __init__(self):
        self.driver = AbstractDriver.get_instance_driver()
        self.gf = GenericFunctions()

    def create_new_group_label(self):
        return self.gf.find_element(xpath="//h5[contains(text(),'Group')]")

    def group_name_input(self):
        return self.gf.find_element(id="group-name")

    def set_group_name(self, groupname):
        self.gf.send_keys(self.group_name_input(), groupname)

    def group_description(self):
        return self.gf.find_element(id="group-description")

    def set_group_description(self, group_description):
        self.gf.send_keys(self.group_description(), group_description)

    def sub_therapy_area(self):
        return self.gf.find_element(css="input[formcontrolname='subTherapeuticArea']")

    def set_sub_therapy_area(self, sub_therpy_area):
        self.gf.send_keys(self.sub_therapy_area(), sub_therpy_area)

    def add_emailid(self):
        return self.gf.find_element(css=".p-chips-input-token>input")

    def set_emailid(self, email_id):
        self.gf.send_keys(self.add_emailid(), email_id)

    def theraputic_area(self):
        return self.gf.find_element(css="select[formcontrolname='therapeuticArea']")

    def region(self):
        return self.gf.find_element(css="select[formcontrolname='region']")

    def time_period(self):
        return self.gf.find_element(css="select[formcontrolname='timePeriod']")

    def create_group_btn(self):
        return self.gf.find_element(css=".buttonCustom")

    @allure.step
    def verify_creategroup_page(self):
        return self.gf.wait_for_element(self.create_new_group_label())

    @allure.step
    def creategroup_mandatory_details(self, name, desription, sub_therapy_area):
        from Utility.fls_page_objects.home_page import HomePage
        self.set_group_name(name)
        self.set_group_description(desription)
        self.set_sub_therapy_area(sub_therapy_area)
        time.sleep(2)
        self.gf.js_click(self.create_group_btn())
        return HomePage()

    @allure.step
    def edit_group(self, desription, email_id):
        from Utility.fls_page_objects.home_page import HomePage
        self.set_emailid(email_id)
        self.set_group_description(desription)
        self.gf.js_click(self.create_group_btn())
        return HomePage()

    @allure.step
    def creategroup_all_details(self, name, desription, sub_therapy_area, email_id):
        from Utility.fls_page_objects.home_page import HomePage
        self.set_emailid(email_id)
        self.set_group_name(name)
        self.set_group_description(desription)
        self.set_sub_therapy_area(sub_therapy_area)
        time.sleep(2)
        self.gf.js_click(self.create_group_btn())
        return HomePage()
