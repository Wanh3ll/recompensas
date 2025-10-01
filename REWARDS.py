import pyautogui
import time
import random

contador = 1
limite = random.randint(40, 60)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(3, 10)/2
time.sleep(10)

from Frases import listaFrases
while contador < limite:
    pyautogui.press("/")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))  
    pyautogui.write(random.choice(list(listaFrases)), interval=(random.randint(1,3)/8))   #normal random.randint(1, 3)/8
    pyautogui.press("enter")
    #pyautogui.sleep(2) # test program ****************************************
    time.sleep(random.randint(15, 30)/2)
    contador += 1
pyautogui.alert("********* CICLO DO CONTADOR COMPLETO *********\n"+"O limite foi de "+str(limite))

#created by @Wanh3ll