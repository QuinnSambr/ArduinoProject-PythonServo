# ArduinoProject-PythonServo
These Scripts were written to interface with a servo motor via a wireless mouse.

Main.cpp is a C++ script that interprelates the data being sent to the arduino from the python script and sending it to the servo.

ArduinoCommands_Send.py is a python script that generates a window and tracks the x,y cords and does a mathematical function that downscales it to degrees of rotation and sends this via serial port to the arduino

Problems:
Arudino Baudrate needs to be at a higher frequency to interprelate the code being parsed faster.

![pt1](https://media.giphy.com/media/TH6QNbdoiki2etLn1n/giphy.gif)
![pt2](https://media.giphy.com/media/low7T3pMC23PAQARV6/giphy.gif)

