from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = '/Users/jamiewhalen/Downloads/chromedriver'
browser = webdriver.Chrome(chromedriver)
browser.get('https://www.bankofamerica.com/')

username = selenium.find_element_by_id("jamielwhalen")
password = selenium.find_element_by_id("Heaven123")

username.send_keys("YourUsername")
password.send_keys("Pa55worD")

selenium.find_element_by_name("submit").click()


