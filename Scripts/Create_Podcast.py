from Base_Setup.Env_Setup import EnvSetup
from Properties.Locators import Locators
import time


class CreatePodcast(EnvSetup):
    def test_CreatePodcast(self):
        self.driver.maximize_window()
        EnvSetup.signIn(self)
        print("Create Podcast")

        self.driver.find_element_by_xpath(Locators.CreatePodcast).click()
        time.sleep(5)
        current_page_title = self.driver.title
        self.driver.find_element_by_xpath(Locators.podcast_name).send_keys("NIkunj Automation ")
        time.sleep(5)

        self.driver.find_element_by_xpath(Locators.podcast_description).send_keys(" ")
        time.sleep(5)
        path = "C:/Nikunj/mumbler/images/podcast-2.jpg"
        EnvSetup.upload_File(self, Locators.uploader, path)

        # Select Category of the Podcast
        category = Locators.category
        category_text = Locators.category_text
        option = "Art"
        EnvSetup.dropdown_selector(self, category, category_text, option)

        # Select Language of the Podcast
        language = Locators.language
        language_text = Locators.language_text
        option = "English"
        EnvSetup.dropdown_selector(self, language, language_text, option)

        self.driver.find_element_by_xpath(Locators.price).send_keys("10")
        self.driver.find_element_by_xpath(Locators.welcome_message).send_keys(
            "This is the Welcome automated welcome message")
        self.driver.find_element_by_xpath(Locators.button_color).send_keys("#717171")
        self.driver.find_element_by_xpath(Locators.text_color).send_keys("#BE0000")
        self.driver.find_element_by_xpath(Locators.website).send_keys("www.nividata.com")
        self.driver.find_element_by_xpath (Locators.instagram).send_keys ("nikunj.91speed")
        self.driver.find_element_by_xpath (Locators.twitter).send_keys ("nikunj91speed")
        self.driver.find_element_by_xpath (Locators.facebook).send_keys ("nikunj.91speed")
        time.sleep(20)
        self.driver.find_element_by_xpath(Locators.save).click()
        time.sleep(100)
        next_page_title = self.driver.title
        EnvSetup.validation(self, current_page_title, next_page_title, "Podcast Created Successfully")
