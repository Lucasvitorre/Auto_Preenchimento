import pyautogui
import pandas as pd
from time import sleep

#importando os AA's
aa= pd.read_csv(r"")
print(aa)

#Pausa Padrão
pyautogui.PAUSE = 3

#abrindo navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
sleep(1)

def cadastrar():

    #click no favorito
    pyautogui.click(x=1018, y=85)
    sleep(1)

    #inserir AA
    pyautogui.click(x=216, y=630)
    
    #Loop para linha
    for linha in aa.index:

        #inserir aa
        pyautogui.click(x=216, y=630)
        pyautogui.write(str(aa.loc[linha,"AA"]))

        #inserir localidade.
        pyautogui.press("tab")  
        pyautogui.press("tab")
        pyautogui.write("*DIADEMA")

        #Clicando na opção com a localidade correta.
        pyautogui.click(x=187, y=536)

        #Inserir Telefone
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.write("11 98694-0062")

        #clique para enviar
        pyautogui.click(x=830, y=636)
        sleep(5)
        #clique para voltar
        pyautogui.click(x=28, y=52)
        sleep (5)
    print("Finalizando o script")

#iniciando função
cadastrar()
