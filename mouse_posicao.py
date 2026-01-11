import pyautogui
import time
import random

c=0
time.sleep(5)
print(pyautogui.position())

while c < 20:
    pyautogui.moveTo(x=(random.randint(1798, 1868)), 
    y=(random.randint(333, 705)), duration=(random.randint(3,6)/5))
    c += 1