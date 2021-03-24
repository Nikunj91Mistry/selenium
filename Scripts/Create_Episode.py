from Base_Setup.Env_Setup import EnvSetup
from Properties.Locators import Locators
from selenium.webdriver.common.keys import Keys
import time


class CreateEpisode(EnvSetup):
    def test_Episode(self):
        EnvSetup.signIn(self)
        time.sleep(5)

        # CLick on the devpodcast
        self.driver.find_element_by_xpath(Locators.dev_podcast).click()
        time.sleep(2)

        # CLick on the New Episode Button
        self.driver.find_element_by_xpath(Locators.new_episode).click()
        time.sleep(2)

        current_page_title = self.driver.title

        # Enter the Episode Name
        self.driver.find_element_by_name(Locators.episode_name).send_keys("New Episode 1")
        time.sleep(5)

        # Upload the Audio file mp3
        path = "C:/Nikunj/mumbler/Sample_Audio/Ik_Onkar.mp3"
        EnvSetup.upload_File(self, Locators.upload_audio, path)
        time.sleep(10)

        # Enter the Episode Descriptions
        self.driver.find_element_by_xpath(Locators.episode_description).send_keys("THis is Episode Descriptions")
        time.sleep(5)

        # Upload the Episode Cover
        path = "C:/Nikunj/mumbler/images/podcast-2.jpg"
        episode_cover = Locators.episode_cover
        EnvSetup.upload_File(self, episode_cover, path)
        time.sleep(5)

        # Select the Episode Type
        # episode_type = Locators.episode_typw
        # episode_type_text = Locators.episode_type_text
        # EnvSetup.dropdown_selector(self, episode_type, episode_type_text, "Private")
        # time.sleep(5)
        self.driver.find_element_by_xpath(Locators.episode_typw).click()
        time.sleep(10)
        print("Click done")
        self.driver.find_element_by_xpath(Locators.episode_type_text).send_keys("Private" + Keys.ENTER)
        print ("Episode Type Selected")

        # Enter the Episode Email Message
        self.driver.find_element_by_xpath(Locators.episode_email_message).send_keys("This is Episode Email Message ")

        # Click on the Episode Publish button
        self.driver.find_element_by_xpath(Locators.publish).click()
        time.sleep(20)

        next_page_title = self.driver.title

        # Validate for the error
        EnvSetup.validation(self, current_page_title, next_page_title, "Episode Created Successfully")
