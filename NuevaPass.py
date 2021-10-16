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

register = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/footer/button")
register.click()
time.sleep(4)

##-----------------------Ingresando a "Mi Cuenta"------------------------------##
perfil = driver.find_element_by_xpath('/html/body/main/div[2]/header/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/div[1]/button').click()
time.sleep(3)

mi_cuenta = driver.find_element_by_xpath('/html/body/main/div[2]/header/div[3]/div[3]/div[2]/div[3]/div[1]/div[1]/div[1]/ul/li[1]').click()
time.sleep(5)

##-----------------------Accediendo a la información del Perfil------------------------------##
informacion= driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section/div[1]/div[1]/a[1]/span').click()


##-----------------------Cambiando Contraseñas------------------------------##
password1 = driver.find_element_by_name("password")
password1.clear()
password1.send_keys("123456")

password_nueva = driver.find_element_by_name("new_password")
password_nueva.clear()
password_nueva.send_keys("hola789123")

terminos= driver.find_element_by_xpath('/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section/form/div[1]/div[9]/div[1]/span/input').click()

guardar = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/section/form/footer/button")
guardar.click()
time.sleep(5)