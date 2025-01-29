import pyautogui
import pandas as pd
from time import sleep

#importando os AA's
aa= pd.read_csv(r"C:\Users\70159006\OneDrive - ArcelorMittal\Documentos\GitHub\Auto_Preenchimento\servicenow\cadastro_maquinas.csv")
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
    sleep(3)
    
    #Loop para linha da tabela
    for linha in aa.index:

        #inserir AA
        pyautogui.click(x=243, y=659)
        
        #inserir aa
        pyautogui.write(str(aa.loc[linha,"AA"]))

        #inserir localidade.
        pyautogui.press("tab")  
        pyautogui.press("tab")
        pyautogui.write("*Longos - FAB TELAS SP")

        #Opção com a localidade correta.
        pyautogui.press("enter")

        #Inserir Telefone
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.write("11 98694-0062")

        #clique para enviar
        pyautogui.press("tab")
        pyautogui.press("enter")
        sleep(6)
    
        #clique para voltar
        pyautogui.click(x=28, y=52)
    print("Finalizando o script")

#Chamando a função
cadastrar()