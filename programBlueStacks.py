import pyautogui
import time
import random

c = 0
l = random.randint(22, 29) 
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(8, 14)/5
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.moveTo(x=1070, y=97, duration=1)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(2,4)/11))
    pyautogui.press("enter")
    time.sleep(random.randint(27, 37)/7)
    c += 1
    time.sleep(random.randint(9, 13)/2)
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
