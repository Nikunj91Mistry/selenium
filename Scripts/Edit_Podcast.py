from Base_Setup.Env_Setup import EnvSetup
from Properties.Locators import Locators
import time


class EditPodcast(EnvSetup):
    def test_edit_podcast(self):
        EnvSetup.signIn(self)
        print("Edit Podcast")

        # click on the podcast Name
        self.driver.find_element_by_xpath(Locators.max_char_podcast).click()
        print(self.driver.title)
        time.sleep(3)
        # Click on the Edit button of the podcast
        self.driver.find_element_by_xpath(Locators.edit_podcast).click()
        print(self.driver.title)
        time.sleep(10)

        # get the value of the podcast name input
        podcast_name = self.driver.find_element_by_xpath(Locators.podcast_name).get_attribute('value')
        print(podcast_name)
        time.sleep(5)

        # get the value of the Podcast description
        podcast_description = self.driver.find_element_by_xpath(Locators.podcast_description).get_attribute('value')
        print(podcast_description)

        # get the value of the Image
        podcast_image = self.driver.find_element_by_xpath(Locators.img_src).get_attribute('src')
        print(podcast_image)

        # get the value of the podcast Category
        podcast_category = self.driver.find_element_by_xpath(Locators.category_value).text
        print(podcast_category)

        # get the value of the podcast language
        podcast_language = self.driver.find_element_by_xpath(Locators.language_value).text
        print(podcast_language)

        # get the value of the podcast price
        podcast_price = self.driver.find_element_by_xpath(Locators.podcast_price).get_attribute('value')
        print(podcast_price)

        # get the value of the welcome message of the podcast
        welcome_message = self.driver.find_element_by_xpath(Locators.welcome_message_value).get_attribute('value')
        print(welcome_message)

        # get the slug of the podcast
        podcast_slug = self.driver.find_element_by_xpath(Locators.podcast_slug_value).get_attribute('value')
        print("https://dev,mumbler.io/" + podcast_slug)

        # get the RSS feed of the podcast
        podcast_rss_feed = self.driver.find_element_by_xpath(Locators.rss_feed).get_attribute('value')
        print(podcast_rss_feed)

        # get the button color
        podcast_button_color = self.driver.find_element_by_xpath(Locators.button_color_value).get_attribute('value')
        print(podcast_button_color)

        # get the button text color
        podcast_button_text_color = self.driver.find_element_by_xpath(Locators.text_color_value).get_attribute('value')
        print(podcast_button_text_color)

        # get website URL
        website_url = self.driver.find_element_by_xpath(Locators.website_value).get_attribute('value')
        print(website_url)

        # get the Instagram username
        insta_url = self.driver.find_element_by_xpath(Locators.instagram_value).get_attribute('value')
        print(insta_url)

        # get the twitter Username
        twitter_url = self.driver.find_element_by_xpath(Locators.twitter_value).get_attribute('value')
        print(twitter_url)

        # get the facebook username
        facebook_url = self.driver.find_element_by_xpath(Locators.facebook_value).get_attribute('value')
        print(facebook_url)
