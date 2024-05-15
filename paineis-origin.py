from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://loger.belgo.com.br/LOGER_WEB/painelPontoCarregamento.html")

#INSERÇÃO DE INFORMAÇÕES

elemento = driver.find_element(By.NAME,"codCentro")
elemento.clear()
time.sleep(2)
elemento.send_keys()

elemento1 = driver.find_element(By.NAME,"codPC")
elemento1.clear()
time.sleep(2)
elemento1.send_keys()

elemento2 = driver.find_element(By.NAME,"pageSize")
elemento2.clear()
time.sleep(2)
elemento2.send_keys()

elemento3 = driver.find_element(By.NAME,"pageSize2")
elemento3.clear()
time.sleep(2)
elemento3.send_keys()

elemento4 = driver.find_element(By.NAME,"refreshTime")
elemento4.clear()
time.sleep(2)
elemento4.send_keys()

elemento5 = driver.find_element(By.XPATH,'//*[@id="configuracao"]/table/tbody/tr/td/table/tbody/tr[8]/td[2]/input[1]')
time.sleep(2)
elemento5.click()


elemento6 = driver.find_element(By.XPATH,'//*[@id="configuracao"]/table/tbody/tr/td/table/tbody/tr[10]/td/input')
time.sleep(2)
elemento6.click()

driver.fullscreen_window()

#DEIXANDO 24 HORAS ABERTA
delay = time.sleep(86400)