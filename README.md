# ArduinoProject-PythonServo
These Scripts were written to interface with a servo motor via a wireless mouse.

Main.cpp is a C++ script that interprelates the data being sent to the arduino from the python script and sending it to the servo.

ArduinoCommands_Send.py is a python script that generates a window and tracks the x,y cords and does a mathematical function that downscales it to degrees of rotation and sends this via serial port to the arduino

Problems:
Arudino Baudrate needs to be at a higher frequency to interprelate the code being parsed faster.

<div style="width:260px;max-width:100%;"><div style="height:0;padding-bottom:177.69%;position:relative;"><iframe width="260" height="462" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/47w1lx"></iframe></div><p><a href="https://imgflip.com/gif/47w1lx">via Imgflip</a></p></div>
