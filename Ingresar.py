import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://aws.pesaschile.cl/iniciar-sesion?back=my-account/")
time.sleep(5)

##-----------------------Inicio de Sesión------------------------------##
user = driver.find_element_by_name("email")
user.clear()
user.send_keys("eupphory@gmail.com")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("123456")

ingresar = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/footer/button")
ingresar.click()

time.sleep(5)