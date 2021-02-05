""" EE 250L Lab 02: GrovePi Sensors


List team members here.
Payton Janish

Insert Github repository link here.
https://github.com/usc-ee250-spring2021/lab02-pjanish
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    USR_PORT = 4    # D4
    RAS_PORT = 0    # A0

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        threshold_dist = grovepi.analogRead(RAS_PORT)
        object_dist = grovepi.ultrasonicRead(USR_PORT)
        close = False

        if(object_dist <= threshold_dist):
             close = True
        if(close):
            setRGB(255,0,0)
            word = str(threshold_dist) + "cm OBJ PRES\n" + str(object_dist) + "cm"
            setText(word)
        else:
            setRGB(0,255,0)
            new_word = str(threshold_dist) + "cm\n" + str(object_dist) + "cm"
            setText(new_word)

