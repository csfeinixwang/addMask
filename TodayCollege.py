from selenium import webdriver
import time


url="https://admin.campushoy.com/index.html#/login"
driver=webdriver.Chrome(executable_path='chromedriver.exe')
time.sleep(1)

driver.maximize_window()
driver.get(url)
time.sleep(1)
login=driver.find_element_by_xpath("//div[@class='switch-box']").click()
