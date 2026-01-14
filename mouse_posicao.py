import pyautogui
import time
import random

c=0
time.sleep(5)
print(pyautogui.position())

while c < 20:
    pyautogui.moveTo(x=(random.randint(667, 1247)), 
    y=(random.randint(166, 190)), duration=(random.randint(3,6)/2.5))
    c += 1