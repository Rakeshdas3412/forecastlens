from Utility.generic_function import AbstractDriver
from selenium.webdriver.chrome.service import Service
from Utility.data_factory.environment import Environment
import time
import configparser
import allure
from Utility.generic_function import GenericFunctions
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import sys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER


class AppManager:

    load_run_config = {
        "fls_app_url": "",
        "browser": "",
    }

    def __init__(self, new_session=""):
        self.load_config()
        if new_session == "close":
            try:
                AbstractDriver.get_instance_driver().close()
                AbstractDriver.get_instance_driver().quit()
            except:
                print("\nNo Instance of Webdriver to Quit")

        elif not new_session == "":
            try:
                AbstractDriver.get_instance_driver().close()
                AbstractDriver.get_instance_driver().quit()
                AbstractDriver.INSTANCE = AbstractDriver.INSTANCE - 1
                AbstractDriver.DRIVER_STATUS = AbstractDriver.NONE
            except:
                print("\nNo Instance of Webdriver to Quit")
                time.sleep(1)
                self.driver = self.init_driver()
                AbstractDriver.INSTANCE = AbstractDriver.INSTANCE + 1
                AbstractDriver.DRIVER = self.driver
                AbstractDriver.DRIVER_STATUS = AbstractDriver.ACTIVE
            if AbstractDriver.INSTANCE <= 0 or AbstractDriver.DRIVER_STATUS == AbstractDriver.NONE:
                self.driver = self.init_driver()
                AbstractDriver.INSTANCE = AbstractDriver.INSTANCE + 1
                AbstractDriver.DRIVER = self.driver
                AbstractDriver.DRIVER_STATUS = AbstractDriver.ACTIVE
            else:
                self.driver = AbstractDriver.get_instance_driver()

    def load_config(self):
        # SingletonDataManager() #To setup testdata
        if AbstractDriver.IS_SESSION_INVOKED is not True:
            print(AppManager.load_run_config['browser'])
            AppManager.load_run_config['fls_app_url'] = self.get_fls_app_url(
            )
            AppManager.load_run_config['browser'] = self.get_browser()
            AbstractDriver.IS_SESSION_INVOKED = True

    def config_files(self):
        #    all_files = {}
        config_file = configparser.ConfigParser()
        config_file.read('config.ini')

        #    all_files['config'] = config_file
        return config_file

    def get_browser(self):
        browser_name = self.config_files()['browser_type']['browser']
        # return self.config_files()['browser_path'][browser_name]
        return browser_name

    def get_fls_app_url(self):
        url = self.config_files()['run_envt']['envt']
        print("Running Environment = "+self.config_files()['envt_url'][url])
        return self.config_files()['envt_url'][url]

    @allure.step
    def launch_fls(self, envt=None):
        from Utility.fls_page_objects.login_page import LoginPage

        if envt is not None:
            if envt == "DEV":
                LOGGER.setLevel(logging.WARNING)
                LOGGER.setLevel(logging.INFO)
                self.driver.get(
                    "https://dev-forecastlens.apps-evalueserve.com/")
                self.driver.set_page_load_timeout(
                    AbstractDriver.PAGE_LOAD_TIMEOUT)
                self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
                return LoginPage()

            elif envt == "QA":
                self.driver.get(
                    "https://qa-forecastlens.apps-evalueserve.com/")
                # GenericFunctions.wait_for_page_load()
                self.driver.set_page_load_timeout(
                    AbstractDriver.PAGE_LOAD_TIMEOUT)
                GenericFunctions.wait_for_page_load()
                self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
                return LoginPage()

            elif envt == "PROD":
                self.driver.get(
                    "https://fl.apps-evalueserve.com/")
                # GenericFunctions.wait_for_page_load()
                self.driver.set_page_load_timeout(
                    AbstractDriver.PAGE_LOAD_TIMEOUT)
                GenericFunctions.wait_for_page_load()
                self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
                return LoginPage()
            else:
                self.driver.get(
                    "https://dev-forecastlens.apps-evalueserve.com/")
                # GenericFunctions.wait_for_page_load()
                self.driver.set_page_load_timeout(
                    AbstractDriver.PAGE_LOAD_TIMEOUT)
                GenericFunctions.wait_for_page_load()
                GenericFunctions.wait_until_spinner_disappeared()
                self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
                GenericFunctions.handle_annoucement()
                return LoginPage()

        elif "PROD" in str(sys.argv):
            print(Environment.PRODUCTION)
            self.driver.get(Environment.PRODUCTION)
            GenericFunctions.wait_for_page_load()
            GenericFunctions.wait_until_spinner_disappeared()
            self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
            return LoginPage()
        elif "DEV" in str(sys.argv):
            print(Environment.DEV)
            self.driver.get(Environment.DEV)
            GenericFunctions.wait_for_page_load()
            self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
            return LoginPage()

        elif "QA" in str(sys.argv):
            print(Environment.QA)
            self.driver.get(Environment.QA)
            GenericFunctions.wait_for_page_load()
            self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
            return LoginPage()
        else:
            print(self.load_run_config['fls_app_url'])
            self.driver.get(self.load_run_config['fls_app_url'])
            GenericFunctions.wait_for_page_load()
            self.driver.implicitly_wait(AbstractDriver.IMPLICIT_TIMEOUT)
            return LoginPage()

    def init_driver(self):
        AbstractDriver.IS_VIEW_SELECTED = False
        browser = AppManager.load_run_config['browser']
        print("\nBrowser="+browser)
        try:
            AbstractDriver.get_instance_driver().quit()
        except:
            pass
        if browser == AbstractDriver.CHROME:
            chrome_options = Options()
            chrome_options.add_experimental_option('prefs', {
                                                   'credentials_enable_service': False, 'profile': {'password_manager_enabled': False}})
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_experimental_option(
                "excludeSwitches", ["enable-automation"])
            chrome_options.add_argument("--ignore-certificate-errors")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--dns-prefetch-disable")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--incognito")
            # chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])
            # chrome_options.add_argument("--start-maximized")
            print("################################")
            #web_driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
            #web_driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
            #web_driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)
            web_driver = webdriver.Chrome(service=Service(
                ChromeDriverManager().install()), options=chrome_options)
            #web_driver = webdriver.Chrome(executable_path="./chromedriver_linux", options=chrome_options)
            web_driver.set_window_size(1360, 768)
            executor_url = web_driver.command_executor._url
            session_id = web_driver.session_id
            print("\n******************************************")
            print(session_id)
            # web_driver.maximize_window()
            return web_driver
        if browser == AbstractDriver.IPAD:
            device_metrics = {
                "width": 768,
                "height": 1024,
                "pixelRatio": 2
            }
            mobile_emulation = {"deviceName": "iPad",
                                # "userAgent": "Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53"
                                }
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option(
                "mobileEmulation", mobile_emulation)
            chrome_options.add_argument(
                "--user-agent=Mozilla/5.0 (iPad; CPU OS 7_0 like Mac OS X) AppleWebKit/537.51.1 (KHTML, like Gecko) Version/7.0 Mobile/11A465 Safari/9537.53")
            chrome_options.add_argument("--show-device-frame")
            chrome_options.add_experimental_option(
                'excludeSwitches', ['enable-logging'])
            web_driver = webdriver.Chrome(
                executable_path="./chromedriver.exe", options=chrome_options)
            web_driver.maximize_window()
            return web_driver
        if browser == AbstractDriver.EDGE:
            web_driver = webdriver.Edge(
                executable_path="./edgedriver.exe")
            web_driver.maximize_window()
            return web_driver
        if browser == AbstractDriver.FIREFOX:
            cap = DesiredCapabilities().FIREFOX
            cap["marionette"] = False
            profile = FirefoxProfile()
            profile.accept_untrusted_certs = True
            profile.assume_untrusted_cert_issuer = True
            #web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
            web_driver = webdriver.Firefox(
                executable_path="./geckodriver", firefox_profile=profile, capabilities=cap)
            web_driver.maximize_window()
            return web_driver
        if browser == AbstractDriver.HEADLESS:
            profile = FirefoxProfile()
            profile.accept_untrusted_certs = True
            options = FirefoxOptions()
            options.add_argument("--headless")
            options.add_argument("--ignore-certificate-errors")
            web_driver = webdriver.Firefox(
                executable_path="./geckodriver", firefox_options=options, firefox_profile=profile)
            return web_driver
        if browser == AbstractDriver.OPERA:
            chrome_options = Options()
            chrome_options.add_argument('--ignore-certificate-errors')
            web_driver = webdriver.Opera(
                executable_path="./operadriver.exe", options=chrome_options)
            web_driver.maximize_window()
            return web_driver
        else:
            chrome_options = webdriver.ChromeOptions()
            web_driver = webdriver.Chrome(
                executable_path="./chromedriver.exe", options=chrome_options)
            web_driver.maximize_window()
            return web_driver

    @staticmethod
    def close_browser(self):
        self.get_instance_driver().close()
        self.get_instance_driver().quit()
        AbstractDriver.INSTANCE = AbstractDriver.INSTANCE - 1
        AbstractDriver.DRIVER_STATUS = AbstractDriver.NONE
