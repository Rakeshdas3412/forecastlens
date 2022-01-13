from Utility.app_maneger import GenericFunctions, AbstractDriver


class DataConfiguration:

    def __init__(self):
        self.driver = AbstractDriver.get_instance_driver()
        self.gf = GenericFunctions()

    def data_configuration_loc(self):
        return self.gf.find_element(xpath="//h5[text()='Data Configuration']")

    def add_new_level_loc(self):
        return self.gf.find_element(css=".addLevelBtn")

    def level_enable_loc(self, level):
        return self.gf.find_element(xpath="//td[contains(text(),'"+level+"')]")

    def levelname_input_loc(self, level):
        return self.gf.find_element(xpath="//td[contains(text(),'"+level+"')]/..//input[@placeholder='Type Text']")

    def segment_input_loc(self, level):
        return self.gf.find_element(xpath="//td[contains(text(),'"+level+"')]/..//input[@type='number']")

    def listbox_loc(self, level):
        return self.gf.find_elements(xpath="//td[contains(text(),'"+level+"')]/..//div[@role='button']")

    def verify_data_configuration_page(self):
        if(self.gf.wait_for_element(self.data_configuration_loc())):
            return True
        else:
            return False

    def verify_level_enable(self, level_name):
        if(self.gf.wait_for_element(self.level_enable_loc(level_name))):
            return True
        else:
            return False
