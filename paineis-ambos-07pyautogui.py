import pyautogui
from time import sleep

#abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
sleep(2)

#maximizar
pyautogui.press("F11")

#inserindo informações
pyautogui.write("")
pyautogui.press("enter")
sleep(3)
pyautogui.click(x=618, y=554)
pyautogui.write("9460")
pyautogui.press("tab")
pyautogui.write("07")
pyautogui.press("tab")
pyautogui.write("20")
pyautogui.press("tab")
pyautogui.write("20")
pyautogui.press("tab")
pyautogui.write("10")
pyautogui.click(x=614, y=671)
sleep(2)
pyautogui.click(x=636, y=711)

#maximizar
pyautogui.press("F11")
