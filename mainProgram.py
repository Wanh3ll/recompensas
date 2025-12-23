# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(62, 69) # reduzir 30 após terminar o dobro de pontos
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(4, 7)/5
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.press("/")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(1,2)/15))
    pyautogui.press("enter")
    time.sleep(random.randint(27, 37)/7)
    c += 1
    pyautogui.hotkey("alt", "home")
    time.sleep(random.randint(3, 7)/2)
    pyautogui.click()    
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
