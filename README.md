# ArduinoProject-PythonServo
These Scripts were written to interface with a servo motor via a wireless mouse.

Main.cpp is a C++ script that interprelates the data being sent to the arduino from the python script and sending it to the servo.

ArduinoCommands_Send.py is a python script that generates a window and tracks the x,y cords and does a mathematical function that downscales it to degrees of rotation and sends this via serial port to the arduino

Problems:
Arudino Baudrate needs to be at a higher frequency to interprelate the code being parsed faster.

<div style="width:100%;height:0px;position:relative;padding-bottom:177.723%;"><iframe src="https://streamable.com/e/jbsm5h" frameborder="0" width="100%" height="100%" allowfullscreen style="width:100%;height:100%;position:absolute;left:0px;top:0px;overflow:hidden;"></iframe></div>
