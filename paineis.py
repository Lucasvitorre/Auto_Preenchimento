from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
#URL PARA ACESSO
driver.get("https://loger.belgo.com.br/LOGER_WEB/painelPontoCarregamento.html")

try:
    wait= WebDriverWait(driver,120)
    driver.implicitly_wait(10)

#PROCURA E INCLUI O VALOR
    #elem= driver.find_element(By.ID, "codCentro").send_keys("9064")
    elem1=driver.find_element(By.NAME, "codPC").send_keys("08")
    elem2=driver.find_element(By.NAME, "pageSize").send_keys("20")
    elem3=driver.find_element(By.NAME, "pageSize2").send_keys("20")
    elem4=driver.find_element(By.NAME, "refreshTime").send_keys("10")

    #assert elem.__getattribute__("9064") == "9064"
    assert elem1.__getattribute__("08") == "08"
    assert elem2.__getattribute__("20") == "20"
    assert elem3.__getattribute__("20") == "20"
    assert elem4.__getattribute__("10") == "10"

finally:
    driver.quit()