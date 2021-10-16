import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://www.pizzahut.es/usuario/inicio")
time.sleep(2)

##-----------------------Inicio de Sesión------------------------------##
user = driver.find_element_by_name("EmailLogin")
user.clear()
user.send_keys("edugar41@gmail.com")

password = driver.find_element_by_name("PasswordLogin")
password.clear()
password.send_keys("hola123456")

#remember = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/form/div[3]/span').click()

register = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/form/button")
register.click()

time.sleep(3)

##-----------------------Ingresando a "Mi Cuenta"------------------------------##
perfil = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]/ul/li[2]/a').click()
time.sleep(2)

mi_cuenta = driver.find_element_by_xpath('/html/body/div[3]/ul/li[2]/a').click()
time.sleep(2)

##-----------------------Accediendo a la información del Perfil------------------------------##
#atras = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div[1]').click()

cambiar_pass= driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(3)

##-----------------------Cambiando Contraseñas------------------------------##
password1 = driver.find_element_by_name("NewPassword")
password1.clear()
password1.send_keys("hola789123")

password_nueva = driver.find_element_by_name("ConfirmNewPassword")
password_nueva.clear()
password_nueva.send_keys("hola789123")

guardar = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/form/div[1]/div[1]/div[1]/button")
guardar.click()

password_confirm = driver.find_element_by_id("passConfirmPopup")
password_confirm.clear()
password_confirm.send_keys("hola123456")

continuar = driver.find_element_by_xpath("/html/body/div[7]/div[1]/div[1]/div[3]/p[2]/a")
continuar.click()
time.sleep(5)