import time
import string  
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)

driver.get("https://www.pizzahut.es/usuario/inicio")
time.sleep(5)

tipo = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[2]/a[2]').click()
time.sleep(2)

email = driver.find_element_by_name("Email")
email.clear()
email.send_keys("edugar41@gmail.com")

telefono = driver.find_element_by_name("FirstPhone")
telefono.clear()
telefono.send_keys("989235595")

password = driver.find_element_by_name("Password")
password.clear()
password.send_keys("hola123456")

password_confirm = driver.find_element_by_name("ConfirmPassword")
password_confirm.clear()
password_confirm.send_keys("hola123456")

time.sleep(2)
politicas= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[3]/div[2]/form/div[5]/span').click()

register = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/div[2]/form/button")
register.click()

time.sleep(5)