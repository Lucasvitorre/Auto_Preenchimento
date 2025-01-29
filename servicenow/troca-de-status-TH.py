import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

th = pd.read_csv("th.csv")
print(th)

#PAUSE PADRÃO 
pyautogui.sleep(1)

#ABRINDO NAVEGADOR

pyautogui.press("win")
pyautogui.write("edge")
sleep(1)
pyautogui.press("enter")
sleep(2)

def cadastrar():

    #click no favorito ativos.
    pyautogui.click(x=410, y=90)
    sleep(2)

    #inserir código TH
    pyautogui.click(x=236, y=268)
    sleep(2)
    #Loop para linha
    for linha in th.index:

        #inserir TH
        pyautogui.click(x=215, y=269)
        
        pyautogui.write(str(th.loc[linha,"Código"]))
        pyautogui.press("enter")
        sleep(3)

        #Clicando no TH escrito anteriormente.
        pyautogui.click(x=175, y=296)
        sleep(2)
        
        #Clicando no status da máquina. 
        pyautogui.click(x=392, y=419)
        sleep(2)

        #Clica no status retired.
        pyautogui.click(x=386, y=571)

        #Clica no Local 
        pyautogui.click(x=976, y=450)
        sleep(2)
        #Clica na localidade correta.
        pyautogui.click(x=981, y=485)
        sleep(2)
        #Clica contratos.
        pyautogui.click(x=200, y=355)
        sleep(2)
        #Clica no campo Comprado.
        pyautogui.click(x=1031, y=388)
        pyautogui.write("*")
        sleep(2)
        #Clica em atualizar, para finalizar.
        pyautogui.click(x=1263, y=175)
        sleep(2)
        #Clicando em voltar, para continuar o loop.
        pyautogui.click(x=26, y=57)



cadastrar()
