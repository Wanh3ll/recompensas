import pyautogui
import random

def moveEdge():   
    resolution = pyautogui.resolution()
    resolutionX1 = int(resolution[0] / 2)
    resolutionX2 = int(resolutionX1 / 4)
    resolutionY1 = int(resolution[1] / 2)
    resolutionY2 = int(resolution[1] / 4 + 200)
    pyautogui.moveTo(random.choice([resolutionX1, resolutionX2]), 
    random.choice([resolutionY1, resolutionY2]), duration = 0.5)
    imagem1 = pyautogui.locateCenterOnScreen("images/edge.png", confidence=0.8, grayscale=False)
    pyautogui.moveTo(imagem1[0] - 200, imagem1[1], duration = 0.5)
    centerImage1 = pyautogui.position()
    centerImage1 = (int(centerImage1[0]), int(centerImage1[1]))
    x1 = centerImage1[0]
    y1 = centerImage1[1]
    position1 = (x1 - 100, y1 - 20)
    position2 = (x1 - 400, y1 + 20)
    newX1 = int(random.choice([position1[0], position2[0]]))
    newY1 = int(random.choice([position1[1], position2[1]]))
    pyautogui.moveTo(newX1, newY1, duration = 0.5)
    pyautogui.click()

def moveBlueStacks():      
    imagem2 = pyautogui.locateCenterOnScreen("images/blueStacks.png", confidence=0.8, grayscale=False)
    pyautogui.moveTo(imagem2[0] - 50, imagem2[1], duration = 0.5)
    centerImage2 = pyautogui.position()
    centerImage2 = (int(centerImage2[0]), int(centerImage2[1]))
    x2 = centerImage2[0]
    y2 = centerImage2[1]
    position3 = (x2 - 100, y2 - 15)
    position4 = (x2 - 300, y2 + 15)
    newX2 = int(random.choice([position3[0], position4[0]]))
    newY2 = int(random.choice([position3[1], position4[1]]))
    pyautogui.moveTo(newX2, newY2, duration = 0.5)
    pyautogui.click()