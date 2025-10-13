import pyautogui
import time
import random
# install "python" extension
# pip install pyautogui

contador = 1
limite = random.randint(40, 60)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(3, 10)/2
time.sleep(10)

from Frases import listaFrases
while contador < limite:
    pyautogui.press("/") # disable in test program
    pyautogui.hotkey("ctrl", "a") # disable in test program
    pyautogui.press("backspace", presses=random.randint(3, 7)) # disable in test program
    #pyautogui.write(random.choice(list(listaFrases)), interval=(random.randint(1,3)/100))   # test program 
    pyautogui.write(random.choice(list(listaFrases)), interval=(random.randint(1,3)/8))   # disable in test program
    pyautogui.press("enter")
    time.sleep(random.randint(15, 30)/2) # disable in test program
    contador += 1
pyautogui.alert("********* CICLO DO CONTADOR COMPLETO *********\n"+"O limite foi de "+str(limite))


                                        #created by @Wanh3ll