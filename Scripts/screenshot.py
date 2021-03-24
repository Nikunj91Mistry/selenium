from Base_Setup.Env_Setup import EnvSetup
import datetime
from selenium import webdriver

driver = webdriver.Chrome (executable_path="../webdrivers/chromedriver_88.0.4324.190.exe")
driver.maximize_window ()

driver.get("https://dev.mumbler.io/")

date = str(datetime.datetime.now()).split('.')[0]
filename = date.replace(" ", "_").replace(":", "_").replace("-", "_")
s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
size = driver.set_window_size(s('Width'), s('Height'))
driver.find_element_by_tag_name('body').screenshot("../Screenshots/" + filename+".png")
