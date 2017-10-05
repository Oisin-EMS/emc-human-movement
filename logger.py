import sys
import thread
import time
import csv

import Leap

logging  = int(raw_input("How many seconds? "))
fileName = raw_input("Filename: ")
dims = int(raw_input("How many dimentions of movenet to record? (1,2 or 3) "))

controller = Leap.Controller()

time.sleep(1)
print "\n\nBegining\n\n"


with open(fileName, "wb") as csvfile:
    if(controller.is_connected):
        for x in xrange(logging * 50):
            dataWriter = csv.writer(csvfile)

            #defines leap objects and gets palm position
            frame = controller.frame()
            hands = frame.hands
            rightHand = hands.rightmost
            position = rightHand.palm_position

            #converts leap vector data to lists of floats
            positionData = position.to_float_array()

            #takes the correct elements of the position, depending on data required
            if dims == 1:
                positionData = [positionData[0]]
            elif dims == 2:
                positionData = [positionData[0], positionData[-1]]
            elif dims == 3:
                pass
            else:
                print "Recording dimentions must be 1, 2 or 3."
                exit()
            
            #prints lists of floats
            print positionData

            #writes float data to a csv
            dataWriter.writerow(positionData)

            #takes position 50 times per second
            time.sleep(0.02)
            
