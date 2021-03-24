import unittest
import time
import datetime
from selenium import webdriver
from Properties.Locators import Locators
from Properties.Id_Passeord import IdPassword
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class EnvSetup(unittest.TestCase):
    def setUp(self):
        print("Setup Function")
        self.driver = webdriver.Chrome(executable_path="../webdrivers/chromedriver_88.0.4324.190.exe")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout (30)

    def tearDown(self):
        print("Teardown Function")
        self.driver.close()

    def signIn(self):
        self.driver.get ("https://dev.mumbler.io/en")
        self.driver.set_page_load_timeout (30)

        self.driver.find_element_by_xpath (Locators.login).click()
        time.sleep (5)

        self.driver.find_element_by_xpath (Locators.login_email).send_keys(IdPassword.nikunj37)
        self.driver.find_element_by_xpath (Locators.login_password).send_keys(IdPassword.password)
        self.driver.find_element_by_xpath (Locators.login_button).click()
        time.sleep (5)

        print (self.driver.title)

    def upload_File(self, Xpath, path):
        self.driver.find_element_by_xpath(Xpath).send_keys(path)
        time.sleep (5)
        print ("File Uploaded")

    def dropdown_selector(self, click_xpath, text_xpath, text):
        # click on the dropdown
        self.driver.find_element_by_xpath(click_xpath).click()
        time.sleep (5)
        # enter the text and select option from the dropdown
        self.driver.find_element_by_css_selector(text_xpath).send_keys(text + Keys.ENTER)

    def take_screenshot(self):
        date = str (datetime.datetime.now ()).split ('.')[0]
        filename = date.replace (" ", "_").replace (":", "_").replace ("-", "_")
        # s = lambda x: self.driver.execute_script ('return document.body.parentNode' + x)
        # size = self.driver.set_window_size (s ('Width'), s ('Height'))
        # self.driver.find_element_by_tag_name ('body').screenshot ("../Screenshots/" + filename + ".png")
        # navbar = self.driver.find_element_by_xpath("//body[1]/div[1]/div[2]/nav[1]")
        # navbar.screenshot("../Screenshots/" + filename + ".jpg")
        self.driver.save_screenshot("../Screenshots/" + filename + ".png")

    def validation(self, current_page_title, next_page_title, success_message):
        if current_page_title != next_page_title:
            print (success_message)
        else:
            try:
                self.driver.find_element_by_xpath(Locators.tost_validation).is_displayed()
                print("Error : " + self.driver.find_element_by_xpath(Locators.tost_validation).text)
            except NoSuchElementException:
                errors = self.driver.find_elements_by_xpath(Locators.username_Validation)
                for error in errors:
                    print("Error : " + error.text)
                EnvSetup.take_screenshot(self)
