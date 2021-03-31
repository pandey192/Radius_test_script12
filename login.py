# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#from cred import name,website,fullName,phone,msg
import time
import uuid

email = uuid.uuid4().hex + '@gmail.com'
# webdriver.Chrome() will be used

driver = webdriver.Chrome(executable_path='/home/shivam/Downloads/pycharm/chromedriver')

# URL of the website
url = "https://app.radiusagent.com/login"

driver.get(url)


driver.find_element_by_xpath('//*[@type= "email"]').send_keys(email)

driver.find_element_by_xpath('//*[@type = "password"]').send_keys(1234)

time.sleep(2)

driver.find_element_by_xpath('/html/body/section/div/div/div/div/div/div/div[2]/div/div/form/div[3]/button').click()


time.sleep(2)



driver.close() 