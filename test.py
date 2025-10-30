# By @Wanh3ll

import pyautogui
import time
import random

c = 0
l = random.randint(1,5)
pyautogui.FAILSAFE = True
pyautogui.PAUSE = (0.5)
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(1,3)/15))
    pyautogui.press("enter")
    c += 1
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
