from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from Base_Setup.Env_Setup import EnvSetup
from Properties.Locators import Locators
import time


class signup(EnvSetup):
    def test_Signup(self):
        self.driver.get("https://dev.mumbler.io/en")
        self.driver.set_page_load_timeout (30)
        time.sleep(5)
        self.driver.find_element_by_xpath(Locators.get_started_button).click()
        time.sleep(5)
        current_page_title = self.driver.title
        print(current_page_title)

        self.driver.find_element_by_xpath(Locators.Signup_name).send_keys("Nikunj")
        time.sleep(5)
        print("Name Entered")
        self.driver.find_element_by_xpath(Locators.Signup_email).send_keys("nikunjm+live6@nividata.com")
        time.sleep(5)
        print("Email Entered")
        self.driver.find_element_by_xpath(Locators.Signup_country).click()
        time.sleep (5)
        self.driver.find_element_by_css_selector("#react-select-2-input").send_keys("Spain" + Keys.ENTER)
        print("Country Selected")
        time.sleep(5)
        action = ActionChains(self.driver)
        checkbox = self.driver.find_element_by_xpath("//input[@id='custom-checkbox']")

        action.move_to_element(checkbox).click().perform()

        self.driver.find_element_by_xpath("//button[contains(text(),'Start my podcast')]").click()
        time.sleep(10)

        next_page_title = self.driver.title

        EnvSetup.validation (self, current_page_title, next_page_title, "Sign Up Success")

        self.driver.find_element_by_xpath(Locators.password1).send_keys("Nikunj@123")
        time.sleep(5)

        self.driver.find_element_by_xpath(Locators.password2).send_keys("Nikunj@123")
        time.sleep(5)

        self.driver.find_element_by_xpath(Locators.start_my_podcast).click()
        time.sleep(5)


        self.driver.find_element_by_xpath("//a[contains(text(),'Close')]").click()

        assert self.driver.page_source.find("A confirmation email has been sent to your inbox. Follow the link in the email to complete your registration.")
