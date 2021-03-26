import unittest
import HtmlTestRunner
import requests
import Env_Setup


class Error_404(Env_Setup.EnvSetup):
    def test_404(self):
        self.driver.get("https://dev.mumbler.io/en")
        self.driver.set_page_load_timeout(60)

        # get all the linkd from the webpage
        all_links = [link.get_attribute("href") for link in self.driver.find_elements_by_xpath("//a[@href]")]

        # get the unique links out of all the links
        unique_links = list(dict.fromkeys(all_links))

        # print all link count
        print("Number of link : %s" %len(all_links))

        # print all unique link count
        print("Number of unique link : %s" %len(unique_links))

        for link in unique_links:
            if link.startswith("https"):
                req = requests.head(link)
                print(link, req.status_code)
            else:
                print("Ignoring '{}'".format(link))


if __name__ == "__main__":
    unittest.main (testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))


# for request module https://2.python-requests.org/en/latest/user/quickstart/
