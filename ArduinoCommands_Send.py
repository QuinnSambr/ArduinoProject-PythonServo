#Written by Quinn Sambrano 
#Version 2.1
#Arduino integration with Python

import pyautogui, sys
from tkinter import * 

#Function tracks X,Y cords in real time within the generated window
def cords(events):
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    label['text']=positionStr
    
#Main function wich generates a window of size 600x600
w=Tk()
canvas=Canvas(width=600,height=600)
label=Label(bd=4 ,bg="white",fg="black")
canvas.bind("<Motion>",cords)
canvas.grid(row=0,column=0)
label.grid(row=1,column=0)
w.mainloop()

