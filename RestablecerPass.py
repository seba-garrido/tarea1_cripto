import time
import string
import random

PATH = "C:\Selenium\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(PATH)
driver.get("https://aws.pesaschile.cl/recuperar-contrase%C3%B1a?token=df0606656972a847fa11372873379377&id_customer=78698&reset_token=5e59a79682a22a6961941245c17dcb461a870ae8")
time.sleep(5)

password1 = driver.find_element_by_name("passwd")
password1.clear()
password1.send_keys("hola789123")

password_nueva = driver.find_element_by_name("confirmation")
password_nueva.clear()
password_nueva.send_keys("hola789123")

cambiar_pass = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/form/section/div[2]/div[3]/div[1]/button")
cambiar_pass.click()
time.sleep(4)
