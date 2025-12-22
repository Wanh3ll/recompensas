# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(65, 75) # reduzir 30 após terminar o dobro de pontos
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(4, 7)/5
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.press("/")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(1,3)/14))
    pyautogui.press("enter")
    time.sleep(random.randint(11, 14)/6)
    c += 1
    time.sleep(1)
    pyautogui.hotkey("alt", "home")
    pyautogui.moveTo(x=1813, y=642, duration=0.2)
    time.sleep(0.3)
    pyautogui.click()    
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
