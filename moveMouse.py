import pyautogui
import random

def fullHD():   
    resolution = pyautogui.resolution()
    resolutionX1 = int(resolution[0] / 2)
    resolutionX2 = int(resolutionX1 / 4)
    resolutionY1 = int(resolution[1] / 2)
    resolutionY2 = int(resolution[1] / 4 + 200)
    pyautogui.moveTo(random.choice([resolutionX1, resolutionX2]), 
    random.choice([resolutionY1, resolutionY2]), duration = 0.5)
    imagem = pyautogui.locateCenterOnScreen("edge.png", confidence=0.8, grayscale=False)
    pyautogui.moveTo(imagem[0] - 200, imagem[1], duration = 0.5)
    centerImage = pyautogui.position()
    centerImage = (int(centerImage[0]), int(centerImage[1]))
    x = centerImage[0]
    y = centerImage[1]
    position1 = (x - 100, y - 20)
    position2 = (x - 400, y + 20)
    newX = int(random.choice([position1[0], position2[0]]))
    newY = int(random.choice([position1[1], position2[1]]))
    pyautogui.moveTo(newX, newY, duration = 0.5)
    pyautogui.click()