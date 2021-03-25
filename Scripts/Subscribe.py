from Base_Setup.Env_Setup import EnvSetup
from Properties.Locators import Locators
import time


class Subscribe(EnvSetup):
    def test_subscribe(self):
        self.driver.set_page_load_timeout(30)
        EnvSetup.signIn(self)
        print("Login Success")
        time.sleep(10)

        # Navigate to home page
        self.driver.find_element_by_xpath(Locators.logo).click()
        time.sleep(10)

        # Click on the 7_dec_podcast_01 podcast page
        self.driver.find_element_by_xpath("//a[@href='/podcast_01']//div").click()
        time.sleep(5)

        # click on the subscribe button
        self.driver.find_element_by_xpath("//a[contains(@class,'btn btn-primary')]").click()
        time.sleep(5)

        # Click on the COnfirmation button
        self.driver.find_element_by_xpath("//button[text()='Subscribe']").click()
        time.sleep(5)

        # enter the card owner name

        self.driver.find_element_by_name("card_owner").send_keys("Nikunj Mistry")
        self.driver.switch_to.frame(0)
        self.driver.find_element_by_name("cardnumber").send_keys("4242 4242 4242 4242")

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(1)
        self.driver.find_element_by_name("exp-date").send_keys(424)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(2)
        self.driver.find_element_by_name("cvc").send_keys("424")

        self.driver.switch_to.default_content()
        EnvSetup.take_screenshot(self)
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'Subscribe')]").click()

        time.sleep(5)
        print(self.driver.title)


