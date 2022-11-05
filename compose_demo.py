# /usr/bin/bash python
# -*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

time.sleep(5)
driver = webdriver.Remote(
    command_executor="http://chrome:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME
)

driver.get("https://www.shopperplus.ca")
content = driver.title.split("_")[0]
print(content)
driver.close()