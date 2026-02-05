import pyautogui
import time
import random
from moveMouse import moveBlueStacks

def blueMain():
    c = 0
    l = random.randint(21, 24) 
    pyautogui.FAILSAFE = True
    #pyautogui.PAUSE = 0.1
    pyautogui.PAUSE = random.randint(8, 12)/12.2
    time.sleep(5)

    from search import phrases
    while c < l:        
        moveBlueStacks()
        pyautogui.hotkey("ctrl", "a")
        pyautogui.press("backspace", presses=random.randint(60, 99))     
        pyautogui.write(random.choice(list(phrases)), interval=(random.randint(2,4)/11.3))
        pyautogui.press("enter")
        time.sleep(random.randint(22, 28)/6.1)
        c += 1
    pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")
