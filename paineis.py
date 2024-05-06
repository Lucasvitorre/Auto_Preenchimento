from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome()

driver.get("https://loger.belgo.com.br/LOGER_WEB/painelPontoCarregamento.html")

#INSERÇÃO 

elemento = driver.find_element(By.NAME,"codCentro")
elemento.clear()
time.sleep(3)
elemento.send_keys("9460")

elemento1 = driver.find_element(By.NAME,"codPC")
elemento1.clear()
time.sleep(3)
elemento1.send_keys("08")

elemento2 = driver.find_element(By.NAME,"pageSize")
elemento2.clear()
time.sleep(3)
elemento2.send_keys("20")

elemento3 = driver.find_element(By.NAME,"pageSize2")
elemento3.clear()
time.sleep(3)
elemento3.send_keys("20")

elemento4 = driver.find_element(By.NAME,"refreshTime")
elemento4.clear()
time.sleep(3)
elemento4.send_keys("10")

elemento5 = driver.find_element(By.XPATH,'//*[@id="configuracao"]/table/tbody/tr/td/table/tbody/tr[10]/td/input')
time.sleep(3)
elemento5.click()

delay = time.sleep(10000)