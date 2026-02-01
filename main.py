from tkinter import Tk, Label, Button
import edge
import blueStacks

window = Tk()
window.title("Recompensas")
window.geometry("640x480")
labelInitial = Label(window, text = "Selecione o programa desejado\n")
labelInitial.pack() 

def button1():  
    print("Script Edge iniciado")  
    edge.main()
    print("Script Edge Finalizado")

button1 = Button(window, text = "EDGE", command = button1)
button1.pack()

def button2():
    print("Script Blue Stacks iniciado")    
    blueStacks.blueMain()
    print("Script Blue Stacks finalizado")

button2 = Button(window, text = "BLUE STACKS", command = button2)
button2.pack()

window.mainloop()