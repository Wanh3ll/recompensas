# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(32, 39)
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
    time.sleep(random.randint(8, 11)/3)
    pyautogui.click()    
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
