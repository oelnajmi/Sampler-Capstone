from threading import Thread

###########################################################################
## To allow this to compile on our computers, the raspberry pi code has been
## commented. When running on a raspberry pi, uncomment all commented code
## and remove all `True` lines for each loop below
###########################################################################

#import RPi.GPIO as GPIO
import time


# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
    
COL = [5,11,9,10]
ROW = [26,19,13,6]


class PadScanner(Thread):
    def __init__(self, interface):
        Thread.__init__(self)
        self.interface = interface
        self.daemon = True
        self.start()

    def run(self):
        for i in range(4):
            True
            #GPIO.setup(ROW[i], GPIO.OUT)
            #GPIO.output(ROW[i], 0)

        for j in range(4):
            True
            #GPIO.setup(COL[j], GPIO.IN)
                
        while True:
            True
            # for i in range(4):
            #     GPIO.output(ROW[i],1)
            #     for j in range(4):
            #         if GPIO.input(COL[j]) == 1:
            #             print("col = " + str((j+1)))
            #             print("row = " + str((i+1)))
            #             print(" ")
            #             self.interface.click_pad(i, j)
            #             time.sleep(0.5)
            #         while(GPIO.input(COL[j]) == 1):
            #             time.sleep (0.2)
            #     GPIO.output(ROW[i],0)

