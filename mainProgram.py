# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(32, 39)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(4, 7)/11.3
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.hotkey("alt", "home")
    pyautogui.moveTo(x=(random.randint(1798, 1868)), 
    y=(random.randint(333, 705)), duration=(random.randint(3,6)/5.2))
    pyautogui.click()
    pyautogui.press("/")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(2,4)/22.7))
    pyautogui.press("enter")
    time.sleep(random.randint(27, 37)/6.4)
    c += 1
    time.sleep(random.randint(8, 11)/6.2)
        
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
