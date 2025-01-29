import pyautogui
import pandas as pd
from time import sleep

#importando os TH's
th= pd.read_csv(r"C:\Users\70159006\OneDrive - ArcelorMittal\Documentos\GitHub\Auto_Preenchimento\servicenow\th.csv")
print(th)

pyautogui.PAUSE = 2

#abrindo navegador
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
sleep(2)

def abrir_requisição():


#clicar no favorito
    pyautogui.click(x=1144, y=89)
    sleep(6)

    for linha in th.index:

        #requisitante
        pyautogui.click(x=187, y=612)

        #Escrever Leonardo como requisitante.
        pyautogui.write("*Carvalho, Leonardo Luiz Gomes De")
        pyautogui.press("enter")
        
        #Avançado para o campo nome do requisitante
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")

        #Inserir nome localidade
        pyautogui.write("*DIADEMA")
        pyautogui.press("enter")

        sleep(1)

        pyautogui.press("tab")
        pyautogui.press("tab")
        sleep(1)

        #Escrever nome do requisitante
        pyautogui.write("Lanes, Lucas Vitor de Oliveira")
        pyautogui.press("tab")
        pyautogui.press("tab")

        # Descrição dos TH e motivo da solicitação.
        texto_concatenado = "Formatacao e configuracao " + str(th.loc[linha, "Código"])
        pyautogui.write(texto_concatenado)
        pyautogui.press("tab")

        #Clique em enviar.      
        pyautogui.press("enter")
        sleep(7)

        #Clique em voltar para o Loop
        pyautogui.click(x=18, y=46)
        sleep(3)
    print("Script Finalizado")

abrir_requisição()