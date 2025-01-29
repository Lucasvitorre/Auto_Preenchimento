from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import traceback
from datetime import datetime

driver = webdriver.Chrome()

driver.get("https://loger.belgo.com.br/LOGER_WEB/painelVeiculosCarregando.html")

def inserir_informacoes():
    try:
        # CENTRO DE CUSTO
        elemento1 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input")
        elemento1.click()
        sleep(1)
        elemento1.send_keys("9460")
        
        # PONTO DE CARREGAMENTO
        elemento2 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr[5]/td[2]/input")
        elemento2.click()
        sleep(1)
        elemento2.send_keys("04")

        # ORDENAÇÃO
        elemento3 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/select")
        dropdown = Select(elemento3)
        dropdown.select_by_value("9")

        # SELECIONAR O DECRESCENTE
        elemento4 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/input[2]")
        elemento4.click()

        #CLICAR EM ENVIAR
        elemento5 = driver.find_element(By.XPATH,"/html/body/div/table/tbody/tr/td/table/tbody/tr[8]/td/input")
        elemento5.click()

        #FULLSCREEN NAVEGADOR
        driver.fullscreen_window()

        #PERMANECER 24H
        sleep(86400)

    except Exception as e:
    # Capturar detalhes do erro
        with open("erro_log.txt", "a") as arquivo:
            arquivo.write(f"Timestamp: {datetime.now()}\n")
            arquivo.write("Ocorreu um erro:\n")
            arquivo.write(str(e) + "\n")  # Apenas a mensagem do erro
            arquivo.write("\nDetalhes do rastreamento de pilha:\n")
            traceback.print_exc(file=arquivo)  # Rastreamento completo no arquivo

    print("Erro registrado em 'erro_log.txt'")

# CHAMANDO FUNCAO PARA INICIAR O SCRIPT
inserir_informacoes()