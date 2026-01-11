import pyautogui
import time
import random

c=0
time.sleep(5)
print(pyautogui.position())

while c < 20:
    pyautogui.moveTo(x=(random.randint(980, 1060)), 
    y=(random.randint(76, 115)), duration=(random.randint(3,6)/2.5))
    c += 1