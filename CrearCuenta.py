import time
import string  
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)

driver.get("https://aws.pesaschile.cl/iniciar-sesion?create_account=1")
time.sleep(5)

#tratamiento = driver.find_element_by_name("id_gender")
#tratamiento.clear()
#tratamiento.send_keys("Sr.")

user = driver.find_element_by_name("firstname")
user.clear()
user.send_keys("seba")

user_lastname = driver.find_element_by_name("lastname")
user_lastname.clear()
user_lastname.send_keys("zoldyck")

email = driver.find_element_by_name("email")
email.clear()
email.send_keys("eupphory@gmail.com")

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("hola123456")

terminos= driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section/form/div[1]/div[8]/div[1]/span/input').click()

register = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section/form/footer/button")
register.click()

time.sleep(5)