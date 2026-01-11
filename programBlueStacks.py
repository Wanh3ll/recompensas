import pyautogui
import time
import random

c = 0
l = random.randint(22, 29) 
pyautogui.FAILSAFE = True
pyautogui.PAUSE = random.randint(8, 12)/13
time.sleep(10)

from search import phrases
while c < l:
    pyautogui.moveTo(x=(random.randint(980, 1060)), 
    y=(random.randint(76, 115)), duration=(random.randint(3,6)/7))
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspace", presses=random.randint(3, 7))     
    pyautogui.write(random.choice(list(phrases)), interval=(random.randint(2,4)/11))
    pyautogui.press("enter")
    time.sleep(random.randint(22, 28)/9)
    c += 1
pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
