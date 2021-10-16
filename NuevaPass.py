import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://aws.pesaschile.cl/recuperar-contrase%C3%B1a/")
time.sleep(5)

user = driver.find_element_by_name("email")
user.clear()
user.send_keys("eupphory@gmail.com")

enviar = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/section/div/button")
enviar.click()

driver.get("https://aws.pesaschile.cl/recuperar-contraseña?token=369287eb97423228135a570a516b3f59&id_customer=51374&reset_token=3ce1ff8287e6cf9396cb04107c834e2f37c2159d")

password_nueva = driver.find_element_by_name("passwd")
password_nueva.clear()
password_nueva.send_keys("contranueva")

password_confirmacion = driver.find_element_by_name("confirmation")
password_confirmacion.clear()
password_confirmacion.send_keys("contranueva")
time.sleep(5)

enviar2 = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/section/div[1]/div[3]/div[1]/button")
enviar2.click()
time.sleep(5)