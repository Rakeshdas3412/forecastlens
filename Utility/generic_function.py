from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import sys
import traceback
import pytest
import os
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from faker import Faker


class AbstractDriver:

    IS_SESSION_INVOKED = False
    PAGE_LOAD_TIMEOUT = 90
    IMPLICIT_TIMEOUT = 15
    CHROME = "chrome"
    FIREFOX = "firefox"
    HEADLESS = "headless"
    HEADLESS_CHROME = "headlesschrome"
    OPERA = "opera"
    EDGE = "edge"
    IPAD = "iPad"
    INSTANCE = 0
    DRIVER = None
    DRIVER_STATUS = ""
    PAGE = None
    ACTIVE = "ACTIVE"
    NONE = ""

    @staticmethod
    def get_instance_driver():
        return AbstractDriver.DRIVER

    @staticmethod
    def get_page_control():
        return AbstractDriver.PAGE

    @staticmethod
    def set_page_control(page):
        AbstractDriver.PAGE = page

    @staticmethod
    def wait_for_element(element):
        try:
            WebDriverWait(AbstractDriver.get_instance_driver(),
                          20).until(ec.visibility_of(element))
            return True
        except:
            return False

    @staticmethod
    def wait_for_page_load():
        try:
            while True:
                if AbstractDriver.get_instance_driver().execute_script("return document.readyState") == "complete":
                    break
        except:
            print("Exception occurred !!!!!!!!!!!!!!!!!")
            pass


class GenericFunctions:

    driver = AbstractDriver.get_instance_driver()

    def __init__(self):
        pass

    def find_element(self=None, xpath=None, css=None, id=None, link_text=None,
                     name=None, tag_name=None, class_name=None, partial_link_text=None, jquery=None):
        try:
            if xpath is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.XPATH, value=xpath)
            if id is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.ID, value=id)
            if name is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.NAME, value=name)
            if link_text is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.LINK_TEXT, value=link_text)
            if css is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.CSS_SELECTOR, value=css)
            if tag_name is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.TAG_NAME, value=tag_name)
            if class_name is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.CLASS_NAME, value=class_name)
            if partial_link_text is not None:
                return AbstractDriver.get_instance_driver().find_element(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)
            if jquery is not None:
                return AbstractDriver.get_instance_driver().execute_script("return $(" + jquery + ").get(0);")
        except:
            print("Unable to find element - %s, %s, %s, %s, %s, %s, %s, %s, %s", xpath, css, id, link_text,
                  name, tag_name, class_name, partial_link_text, jquery)
            return False

    def find_elements(self=None, xpath=None, css=None, id=None, link_text=None,
                      name=None, tag_name=None, class_name=None, partial_link_text=None, jquery=None):
        try:
            if xpath is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.XPATH, value=xpath)
            if id is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.ID, value=id)
            if name is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.NAME, value=name)
            if link_text is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.LINK_TEXT, value=link_text)
            if css is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.CSS_SELECTOR, value=css)
            if tag_name is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.TAG_NAME, value=tag_name)
            if class_name is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.CLASS_NAME, value=class_name)
            if partial_link_text is not None:
                return AbstractDriver.get_instance_driver().find_elements(by=By.PARTIAL_LINK_TEXT, value=partial_link_text)
        except:
            print("Unable to find element - %s, %s, %s, %s, %s, %s, %s, %s, %s", xpath, css, id, link_text,
                  name, tag_name, class_name, partial_link_text, jquery)
            return False

    @staticmethod
    def wait_for_page_load():
        try:
            while True:
                if AbstractDriver.get_instance_driver().execute_script("return document.readyState") == "complete":
                    break
        except:
            print("Exception occurred !!!!!!!!!!!!!!!!!")
            pass

    @staticmethod
    def wait_for_element(element):
        try:
            WebDriverWait(AbstractDriver.get_instance_driver(),
                          20).until(ec.visibility_of(element))
            return True
        except:
            print("wait_for_element function - Unable to find element")

    @staticmethod
    def js_click(element, is_trace_needed=True):
        try:
            AbstractDriver.get_instance_driver().execute_script(
                "arguments[0].click();", element)
        except:
            print("js_click function - Unable to find element")
            GenericFunctions.attach_screen_shot()
            if is_trace_needed is True:
                traceback.print_stack(limit=5)

    @staticmethod
    def js_click_with_focus(element, is_trace_needed=True):
        try:
            GenericFunctions.scroll_to_element(element)
            AbstractDriver.get_instance_driver().execute_script(
                "arguments[0].click();", element)
        except:
            print("js_click function - Unable to find element")
            GenericFunctions.attach_screen_shot()
            if is_trace_needed is True:
                traceback.print_stack(limit=5)

    @staticmethod
    def scroll_top(seconds=0.5):
        try:
            AbstractDriver.get_instance_driver().execute_script(
                "window.scrollTo(document.body.scrollHeight, 0)")
            time.sleep(seconds)
        except:
            print("scroll_top function - Unable to find element")

    @staticmethod
    def send_keys(element, data):
        try:
            element.send_keys(data)
        except:
            print("\nelement not found")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def clear_send_keys(element, data):
        try:
            element.clear()
        except:
            print("\nCan not clear data from element")
            traceback.print_stack(limit=5)
        GenericFunctions.send_keys(element, data)

    @staticmethod
    def attach_screen_shot():
        allure.attach(AbstractDriver.get_instance_driver().get_screenshot_as_png(
        ), name=GenericFunctions.get_random_file_names(), attachment_type=AttachmentType.PNG)

    @staticmethod
    def get_random_file_names():
        fake_data = Faker("uk_uA")
        return (fake_data.text(max_nb_chars=20)).replace(".", "")

    @staticmethod
    def paste_keys(element, data):
        try:
            os.environ['CLIPBOARD'] = data
            element.click()
            element.send_keys(Keys.CONTROL, 'v')
        except:
            print("\nelement not found")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def type_keys(element, data):
        try:
            actions = ActionChains(AbstractDriver.get_instance_driver())
            actions.click(element).perform()
            element.clear()
            actions.send_keys().perform()
        except:
            print("element not found")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def get_textwhith_hover(element, data):
        try:
            actions = ActionChains(AbstractDriver.get_instance_driver())
            actions.click(element).perform()
            element.clear()
            actions.send_keys().perform()
        except:
            print("element not found")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def js_type(element, value):
        try:
            AbstractDriver.get_instance_driver().executeScript(
                "arguments[0].value='" + value + "'", element)
        except:
            print("Unable to type - js_type")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def get_text(element):
        try:
            return element.text
        except:
            print("unable to read from element")

    @staticmethod
    def select_by_text(element, text):
        try:
            select = Select(element)
            select.select_by_visible_text(text)
        except:
            print("Unable to select text by given element")
            GenericFunctions.attach_screen_shot()
            traceback.print_stack(limit=5)

    @staticmethod
    def is_element_exists(xpath, default_time_out=2):
        AbstractDriver.get_instance_driver().implicitly_wait(default_time_out)
        if isinstance(xpath, str):
            try:
                #WebDriverWait(AbstractDriver.get_instance_driver(), default_time_out).until(ec.presence_of_element_located((By.XPATH, xpath)))
                return GenericFunctions.find_element(xpath=xpath).is_displayed()
                #WebDriverWait(AbstractDriver.get_instance_driver(), default_time_out).until(ec.visibility_of(AbstractDriver.get_instance_driver().find_element(by=By.XPATH, value=xpath)))
            except:
                print("Element (string) does not exist - Returning False")
                return False
            finally:
                AbstractDriver.get_instance_driver().implicitly_wait(
                    AbstractDriver.IMPLICIT_TIMEOUT)
        else:
            try:
                return xpath.is_displayed()
            except:
                print("Element does not exist - Returning False")
                return False
            finally:
                AbstractDriver.get_instance_driver().implicitly_wait(
                    AbstractDriver.IMPLICIT_TIMEOUT)

    @staticmethod
    def scroll_to_element(element):
        if isinstance(element, str):
            try:
                GenericFunctions.scroll_top(0)
                #inlineCenter = {behavior: 'smooth', block: 'center', inline: 'start'};
                AbstractDriver.get_instance_driver().execute_script(
                    "arguments[0].scrollIntoView(false);", AbstractDriver.get_instance_driver().find_element(by=By.XPATH, value=element))
                time.sleep(2)
            except:
                print("scroll_to_element function - Unable to find element")
        else:
            try:
                GenericFunctions.scroll_top()
                AbstractDriver.get_instance_driver().execute_script(
                    "arguments[0].scrollIntoView(false);", element)
                time.sleep(1)
            except:
                print("scroll_to_element function - Unable to find element")
