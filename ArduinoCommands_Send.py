#Written by Quinn Sambrano 
#Version 2.1
#Arduino integration with Python

import pyautogui, sys
from tkinter import *
import serial
import time

#Function tracks X,Y cords in real time within the generated window
ser=serial.Serial('COM3',baudrate=57600, timeout=1)

def writePort(arduino_values):
    ser.write(arduino_values.encode())
    time.sleep(0.0125)

def cords(events):
    x, y = pyautogui.position()
    ard_val="X{xaxis}".format(xaxis= 180- x / float((600/170)))
    label['text']=ard_val
    writePort(ard_val)
    
#Main function wich generates a window of size 600x600
w=Tk()
canvas=Canvas(width=600,height=600)
label=Label(bd=4 ,bg="white",fg="black")
canvas.bind("<Motion>",cords)
canvas.grid(row=0,column=0)
label.grid(row=1,column=0)
w.mainloop()

