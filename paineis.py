import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://loger.belgo.com.br/LOGER_WEB/painelPontoCarregamento.html")

elemento_centro = driver.find_elements("codCentro")

ponto_carregamento = driver.find_elements("codPC")

numero_linha = driver.find_elements("pageSize")

numero_linha_2 = driver.find_elements("")

refresh = driver.find_elements("")

apresen_painel = driver.find_elements("")