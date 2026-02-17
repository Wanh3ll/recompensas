import pyautogui
import time
import random
from moveMouse import moveEdge

def edgeMain():    
    c = 0
    l = random.randint(31, 34)
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = random.randint(4, 7)/11.3
    time.sleep(5) 

    from search import phrases
    while c < l:                
        moveEdge()
        pyautogui.press("backspace", presses=random.randint(6, 9))     
        pyautogui.write(random.choice(list(phrases)), interval=(random.randint(2,4)/22.7))
        pyautogui.press("enter")    
        time.sleep(random.randint(27, 37)/6.4)
        c += 1
        time.sleep(random.randint(8, 11)/6.2)  
        pyautogui.hotkey("alt", "home")      
    pyautogui.alert(f"**** COMPLETE COUNTER CICLE ****\nThe limit was {l}")