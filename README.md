# ArduinoProject-PythonServo
These Scripts were written to interface with a servo motor via a wireless mouse.

The first Script Main.cpp is a C++ script that interprelates the data being sent to the arduino from the python script and sending it to the servo.

The second script ArduinoCommands_Send.py is a python script that generates a window and tracks the x,y cords and does a mathematical function that downscales it to degrees of rotation and sends this via serial port to the arduino