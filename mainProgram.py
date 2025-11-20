# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(33, 46)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(7, 16)/3
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.press("/")
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(1,3)/8))
    pyautogui.press("enter")
    time.sleep(random.randint(40, 58)/3)
    c += 1
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
