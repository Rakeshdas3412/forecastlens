from Utility.app_maneger import GenericFunctions, AbstractDriver
import allure
from Utility.fls_page_objects.data_configuration import DataConfiguration


class CreateNewSceanrio:

    def __init__(self):
        self.driver = AbstractDriver.get_instance_driver()
        self.gf = GenericFunctions()

    def create_new_group_loc(self):
        return self.gf.find_element(xpath="//h5[text()='Create New Scenario']")

    def scenario_name_loc(self):
        return self.gf.find_element(id="group-name")

    def set_sceanrio_name(self, sceanrio_input):
        self.gf.send_keys(self.scenario_name_loc(), sceanrio_input)

    def scenario_description_loc(self):
        return self.gf.find_element(id="group-desc")

    def set_description_name(self, description_input):
        self.gf.send_keys(self.scenario_description_loc(), description_input)

    def select_startmonth_loc(self):
        return self.gf.find_element(xpath="//select[@name='start_month']")

    def set_start_month(self, start_month):
        self.gf.select_by_text(self.select_startmonth_loc(), start_month)

    def select_endmonth_loc(self):
        return self.gf.find_element(xpath="//select[@name='end_month']")

    def set_end_month(self, end_month):
        self.gf.select_by_text(self.select_endmonth_loc(), end_month)

    def country_loc(self, country_name):
        return self.gf.find_element(
            xpath="//label[@for='"+country_name+"']/preceding-sibling::p-radiobutton//div[@role='radio']")

    def next_button_loc(self):
        return self.gf.find_element(xpath="//button[@type='submit']")

    @allure.step
    def configure_sceanrio(self, sceanrio_name, scenario_desc, start_month, end_month, country_name):
        self.set_sceanrio_name(sceanrio_name)
        self.set_description_name(scenario_desc)
        self.set_start_month(start_month)
        import pdb
        pdb.set_trace()
        self.set_end_month(end_month)
        self.gf.js_click_with_focus(self.country_loc(country_name))
        self.gf.js_click_with_focus(self.next_button_loc())
        return DataConfiguration()

    def verify_create_new_group(self):
        if(self.gf.wait_for_element(self.create_new_group_loc())):
            return True
        else:
            print("Unable to verify create new group")
