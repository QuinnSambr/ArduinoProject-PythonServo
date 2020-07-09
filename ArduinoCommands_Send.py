# import serial
# import time

# ser=serial.Serial('COM3',baudrate=9600, timeout=1)
# time.sleep(3)
# def getVal():
#     ser.write(b'g') #B is for writing byte
#     ad = ser.readline().decode('ascii')
#     return ad

# while(1):
#     userInput=input('Get Data Point ?\n')

#     if userInput=='y':
#         print(getVal())




import pyautogui, sys
from tkinter import * 
def cords(events):
    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
    label['text']=positionStr
    

w=Tk()
canvas=Canvas(width=600,height=600)
label=Label(bd=4 ,bg="white",fg="black")
canvas.bind("<Motion>",cords)
canvas.grid(row=0,column=0)
label.grid(row=1,column=0)
w.mainloop()
