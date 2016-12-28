#Program by Fares Al Ghazy
#Program to reduce eye-strain, applies 20 20 20 rule, reminds user to look away every 20 minutes for 20 seconds preferably at an object 20m away
#Other projects: https://github.com/Faresalghazy
#-------------------------------------------------------------------------------#

import time,ctypes
from winsound import Beep
#global variable
num_seconds = 1200
#on startup, verify program working
Beep(600,1000)
ctypes.windll.user32.MessageBoxW(0,"Eyebreak works on your device :) \n\nDeveloper:\nwww.github.com/FaresAlGhazy", "Eye break", 0)
    
while True:
    #simple timer function
    start = time.time()
    end = time.time()
    while((end-start )< num_seconds):
        end = time.time()
        #display message
    Beep(600,1000)
    ctypes.windll.user32.MessageBoxW(0,"20 minutes elapsed, please give your eyes a 20 second break \n\nDeveloper:\nwww.github.com/FaresAlGhazy", "Eye break", 0)
    
