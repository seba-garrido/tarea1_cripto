import time
import string
import random
PATH = "C:\Selenium\chromedriver.exe"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://www.pizzahut.es/usuario/inicio")
time.sleep(15)

##-----------------------Inicio de Sesión------------------------------##
user = driver.find_element_by_name("EmailLogin")
user.clear()
user.send_keys("eupphory@gmail.com")

password = driver.find_element_by_name("PasswordLogin")
password.clear()
password.send_keys("hola123456")

remember = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/form/div[3]/span').click()

register = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/form/button")
register.click()

time.sleep(3)