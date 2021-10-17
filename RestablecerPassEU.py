import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://www.pizzahut.es/usuario/inicio")
time.sleep(2)

recuperar = driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[2]/div[3]/div[1]/a').click()


email = driver.find_element_by_name("ForgottenPasswordEmail")
email.clear()
email.send_keys("seba-garrido@hotmail.com")

recuperar_pass = driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/div[3]/form/button")
recuperar_pass.click()
time.sleep(4)