from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("GRAFANADATAURL")
driver.implicitly_wait(12.5)
username = driver.find_element_by_class_name("css-yn255a-input-input")
password = driver.find_element_by_id("current-password")
username.send_keys("XXX")
password.send_keys("XXX")
driver.find_element_by_class_name("css-14g7ilz-button").click()
driver.implicitly_wait(10.0)
driver.find_element_by_class_name("css-1i6bacp").click()
driver.find_element_by_class_name("css-uvldi-input-suffix").click()
driver.find_element_by_xpath(".//*[contains(text(), 'Series joined by time')]").click()
driver.find_element_by_class_name("css-obkt16-button").click()
driver.quit()
