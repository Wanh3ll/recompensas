import pyautogui
import time
import random
# install "python" extension
# pip install pyautogui

contador = 1
limite = random.randint(10, 16)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(3, 10)/2
time.sleep(10)

from Frases import listaFrases
while contador < limite:
    pyautogui.write(random.choice(list(listaFrases)), interval=(random.randint(1,3)/100)) 
    pyautogui.write(random.choice(list(listaFrases)), interval=(random.randint(1,3)/8))
    pyautogui.press("enter")
    contador += 1
pyautogui.alert("********* CICLO DO CONTADOR COMPLETO *********\n"+"O limite foi de "+str(limite))


                                            #created by @Wanh3ll