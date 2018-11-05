#########################################################################
# Date: 2018/10/02
# file name: 1st_assignment_main.py
# Purpose: this code has been generated for the 4 wheels drive body
# moving object to perform the project with ultra sensor
# this code is used for the student only
#########################################################################
from SEN040134 import SEN040134_Tracking as Tracking_Sensor
from car import Car
import time
import RPi.GPIO as GPIO 


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()
        

    # =======================================================================
    # 1ST_ASSIGNMENT_CODE
    # Complete the code to perform First Assignment
    # =======================================================================
    def car_startup(self):
        # Implement the assignment code here.
        self.car.accelerator.go_forward(60)
       
        while True:
            list = self.car.line_detector.read_digital()
            l_list = []
            for i in range(100):
                l_list.append(list)
            time.sleep(0.01)
            
            if list == [0, 1, 1, 0, 0]:
                self.car.steering.turn_left(80)
                time.sleep(0.01)
            elif l_list[i] == [1, 0, 0, 0, 0]:
                if l_list[i-1] == [1, 1, 0, 0, 0] or [1, 0, 0, 0, 0]:
                    self.car.steering.turn_left(60)
                    time.sleep(0.01)

            elif list == [0, 0, 1, 1, 0]:
                self.car.steering.turn_right(100)
                time.sleep(0.01)
            elif l_list[i] == [0, 0, 0, 0, 1]:
                if l_list[i-1] == [0, 0, 0, 1, 1] or [0, 0, 0, 0, 1]:
                    self.car.steering.turn_right(120)
                    time.sleep(0.01)
            elif list == [0, 0, 1, 0, 0]:
                self.car.steering.turn(90)
            elif list == [0, 0, 0, 0, 0]:
                self.car.accelerator.stop()
                time.sleep(0.01)
                break
            else:
                time.sleep(0.01)

if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
