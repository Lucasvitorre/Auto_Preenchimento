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

#
#clicar no favorito
    pyautogui.click(x=1144, y=89)
    sleep(6)

    for linha in th.index:

        #Clicar no campo do localidade
        pyautogui.click(x=240, y=620)

        #Inserir nome localidade
        pyautogui.write("*DIADEMA")
        pyautogui.click(x=193, y=575)   

        sleep(1)

        #Avançado para o campo nome do requisitante
        pyautogui.press("tab")
        pyautogui.press("tab")

        #Escrever Leonardo como requisitante.
        pyautogui.write("Carvalho, Leonardo Luiz Gomes De")

        pyautogui.press("tab")
        pyautogui.press("tab")
        sleep(1)

        # Descrição dos TH e motivo da solicitação.
        texto_concatenado = "Formatacao e configuracao " + str(th.loc[linha, "Código"])
        pyautogui.write(texto_concatenado)
        pyautogui.press("tab")

        #Clique em enviar.      
        pyautogui.press("enter")
        sleep(7)

        #Clique em voltar para o Loop
        pyautogui.click(x=22, y=54)
        sleep(3)
    print("Script Finalizado")

abrir_requisição()