import time

from Scripts.Env_Setup import EnvSetup
from Scripts.Locators import Locators
import Id_Passeord


class Singin(EnvSetup):
    def test_singin(self):
        self.driver.get("https://dev.mumbler.io/en")
        self.driver.set_page_load_timeout(30)

        self.driver.find_element_by_xpath(Locators.login).click()
        time.sleep(5)
        login_page_title = self.driver.title

        self.driver.find_element_by_xpath(Locators.login_email).send_keys(Id_Passeord.IdPassword.nikunj37)
        self.driver.find_element_by_xpath(Locators.login_password).send_keys(Id_Passeord.IdPassword.password)
        self.driver.find_element_by_xpath(Locators.login_button).click()
        time.sleep(5)
        print(self.driver.get_cookies())

        current_page_title = self.driver.title

        # if login_page_title == current_page_title:
        #     try:
        #         self.driver.find_element_by_xpath(Locators.tost_validation).is_displayed()
        #         print("Error : " + self.driver.find_element_by_xpath(Locators.tost_validation).text)
        #     except NoSuchElementException:
        #         errors = self.driver.find_elements_by_xpath(Locators.username_Validation)
        #         for error in errors:
        #             print("Error : " + error.text)
        # else:
        #     print("Login Success")
