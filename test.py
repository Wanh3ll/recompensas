# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(10,20)
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
    time.sleep(random.randint(27, 37)/4)
    c += 1   
    time.sleep(random.randint(15, 19)/6) # compensa o restante do código removido
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
