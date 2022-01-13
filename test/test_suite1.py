from threading import settrace
import pytest
import allure
from Utility.app_maneger import AppManager
from Utility.data_factory.login_page_data import LoginPage_Data
from Utility.data_factory.creategroup_data import CreategroupData
from Utility.data_factory.create_new_sceanrio import CreateNewSceanrio
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

import time


class TestScenario:

    @allure.testcase("TC-01=Verify login function for extenral user")
    @allure.testcase("TC_02=Verify logout funciton for external user")
    def test_logout_function(self):
        # Login to applicaiton
        username = LoginPage_Data().evs_login["username"]
        password = LoginPage_Data().evs_login["password"]
        HomePage = AppManager(1).launch_fls(
        ).login_as_externalUser(username, password)
        assert HomePage.validate_homepage() == True
        # Logout to applicaiton
        LoginPage = HomePage.click_logout()
        assert LoginPage.verify_loginpage() == True

    @allure.testcase("TC_04 =Verify create new group with mandatory details")
    def test_create_group_mandatorydetails(self):
        username = LoginPage_Data().evs_login["username"]
        password = LoginPage_Data().evs_login["password"]
        # Launch Browser and login to app
        HomePage = AppManager(1).launch_fls(
        ).login_as_externalUser(username, password)
        assert HomePage.validate_homepage() == True
        CreateGroup = HomePage.click_on_creategroup()

        # Verify create group page
        assert CreateGroup.verify_creategroup_page() == True
        group_mandatory_data = CreategroupData.generate_group_mandatory_details(
            CreategroupData.createGrp_mandatorydetails)
        group_name = group_mandatory_data["group_name"]
        group_description = group_mandatory_data["group_description"]
        sub_therapy_area = group_mandatory_data["sub_therapy_area"]
        HomePage1 = CreateGroup.creategroup_mandatory_details(
            group_name, group_description, sub_therapy_area)
        # Verify HomePage
        time.sleep(10)
        assert HomePage1.validate_homepage() == True

        assert HomePage1.validate_homepage() == True
        assert HomePage1.delete_group(group_name) == True

    @allure.testcase("TC_04 =Verify create new group with all details")
    def test_create_group_alldetails(self):
        username = LoginPage_Data().evs_login["username"]
        password = LoginPage_Data().evs_login["password"]
        # Launch Browser and login to app
        HomePage = AppManager(1).launch_fls(
        ).login_as_externalUser(username, password)
        assert HomePage.validate_homepage() == True
        CreateGroup = HomePage.click_on_creategroup()

        # Verify create group page
        assert CreateGroup.verify_creategroup_page() == True
        group_all_data = CreategroupData.generate_grp_alldetails(
            CreategroupData.createGrp_all_details)
        group_name = group_all_data["group_name"]
        group_description = group_all_data["group_description"]
        sub_therapy_area = group_all_data["sub_therapy_area"]
        email_id = group_all_data["email_id"]

        HomePage = CreateGroup.creategroup_all_details(
            group_name, group_description, sub_therapy_area, email_id)
        # Verify HomePage
        time.sleep(10)
        assert HomePage.validate_homepage() == True
        CreateGroup = HomePage.click_on_edit_icon(group_name)
        assert CreateGroup.verify_creategroup_page() == True
        group_description1 = group_all_data["group_description"]
        email_id1 = group_all_data["email_id"]
        HomePage = CreateGroup.edit_group(group_description1, email_id1)
        assert HomePage.validate_homepage() == True
        assert group_description1 in HomePage.get_group_description(group_name)

        assert HomePage.delete_group(group_name) == True

    @allure.testcase("Verify configure scenario feature with starts month as Sept-14 and end month as July -22 for annual data")
    def test_configure_sceanrio_annnualdata(self):
        username = LoginPage_Data().evs_login["username"]
        password = LoginPage_Data().evs_login["password"]
        # Launch Browser and login to app
        HomePage = AppManager(1).launch_fls(
        ).login_as_externalUser(username, password)
        assert HomePage.validate_homepage() == True
        CreateGroup = HomePage.click_on_creategroup()
        LOGGER.setLevel(logging.WARNING)
        LOGGER.setLevel(logging.INFO)

        # Verify create group page
        assert CreateGroup.verify_creategroup_page() == True
        group_all_data = CreategroupData.generate_grp_alldetails(
            CreategroupData.createGrp_all_details)
        group_name = group_all_data["group_name"]
        group_description = group_all_data["group_description"]
        sub_therapy_area = group_all_data["sub_therapy_area"]
        email_id = group_all_data["email_id"]

        HomePage = CreateGroup.creategroup_all_details(
            group_name, group_description, sub_therapy_area, email_id)
        # Verify HomePage
        assert HomePage.validate_homepage() == True
        CreateNewGroup = HomePage.click_on_define_sceanrio(group_name)

        # Verify Create new sceanrio page
        assert CreateNewGroup.verify_create_new_group() == True
        scenario_data = CreateNewSceanrio.generate_new_scenario_data(
            CreateNewSceanrio.create_new_sceanario)
        sceanario_name = scenario_data["scenario_name"]
        sceanario_desc = scenario_data["scenario_desc"]
        start_month = scenario_data["start_month"]
        end_month = scenario_data["end_month"]
        country = scenario_data["country_name"]

        start_month = scenario_data["start_month"]
        DataConfiguration = CreateNewGroup.configure_sceanrio(
            sceanario_name, sceanario_desc, start_month, end_month, country)

        # Verify Data Configuration page
        assert DataConfiguration.verify_data_configuration_page() == True
        # Click on add another level
        DataConfiguration.add_new_level_loc()
        assert DataConfiguration.verify_level_enable("Level 3") == True

        

    @allure.testcase("Close browser")
    def test_close_browser(self):
        AppManager("close")
