from Base_Setup.Env_Setup import EnvSetup
import time


class Launch(EnvSetup):
    def test_launch(self):
        self.driver.get("https://mumbler.io/en")
        time.sleep(5)
        print (self.driver.title)

        self.driver.find_element_by_xpath("//a[contains(text(),'Manifesto')]").click()
        print(self.driver.title)
        time.sleep(2)

        self.driver.find_element_by_xpath("//a[contains(text(),'Team')]").click()
        print(self.driver.title)
        time.sleep (2)

        self.driver.find_element_by_xpath("//a[contains(text(),'Legal')]").click()
        print(self.driver.title)
        time.sleep(3)

        self.driver.find_element_by_xpath("//a[contains(text(),'Help')]").click()
        print(self.driver.title)
        time.sleep(3)