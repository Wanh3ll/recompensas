from tkinter import Tk, Label, Button
import pyautogui
import edge
import blueStacks


res = (pyautogui.size())
if res <= (1920, 1080):
    resS = 350, 200
    print(f"Resolução: {res[0]}x{res[1]}")
elif res > (1920, 1080):
    resS = 800, 400
    print(f"Resolução: {res[0]}x{res[1]}")
window = Tk()
window.title("Recompensas")
window.geometry(f"{resS[0]}x{resS[1]}")
labelInitial = Label(window, text = "\nSelecione o programa desejado\n", font = ("Arial", 12))
labelInitial.pack() 

def button1():  
    print("Script Edge iniciado")  
    edge.edgeMain()
    print("Script Edge Finalizado")

button1 = Button(window, text = " EDGE ", command = button1)
button1.pack()

def button2():
    print("Script Blue Stacks iniciado")    
    blueStacks.blueMain()
    print("Script Blue Stacks finalizado")

button2 = Button(window, text = " BLUE STACKS ", command = button2)
button2.pack()

window.mainloop() 