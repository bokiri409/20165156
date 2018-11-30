#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        # implement the assignment code here
        # self.car.accelerator.stop()
        self.car.accelerator.go_forward(37)

        while True:
            distance = self.car.distance_detector.get_distance()
            list = self.car.line_detector.read_digital()
            inline = self.car.line_detector.is_in_line()
            angle = self.car.steering.turning_offset
            count = 0
            print(angle)
            print(list)


            if list == [1, 1, 1, 1, 1]:
                if count == 4:
                    self.car.accelerator.stop()
                    break
                    # 장애물 4번 넘고 stop
            elif list == [0, 0, 0, 0, 0]:
                # self.car.steering.center_alignment()
                if angle >= 90:
                    self.car.steering.turn(180-angle)
                else:
                    self.car.steering.turn(90+angle)
                self.car.accelerator.go_backward(37)
                time.sleep(0.1)
                #라인 벗어났을 때 30의 속도로 후진하기
            elif list == [0, 1, 1, 0, 0]:
                self.car.steering.turn_left(80)
                self.car.accelerator.go_forward(37)
                time.sleep(0.1)
            elif list == [1, 0, 0, 0, 0]:
                self.car.steering.turn_left(60)
                self.car.accelerator.go_forward(37)
                time.sleep(0.1)
            elif list == [0, 0, 1, 1, 0]:
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(37)
                time.sleep(0.1)
            elif list == [0, 0, 0, 0, 1]:
                self.car.\
                    steering.turn_right(120)
                self.car.accelerator.go_forward(37)
                time.sleep(0.1)
            elif list == [0, 0, 1, 0, 0]:
                self.car.steering.center_alignment()
                self.car.accelerator.go_forward(37)
                time.sleep(0.1)
            else:
                time.sleep(0.1)

            #장애물을 만났을 때 운행 따로 진행
            while distance <= 25 & distance >= 0: #장애물과의 거리가 30이하일때
                # list1 = self.car.line_detector.read_digital()
                self.car.accelerator.go_forward(35)
                self.car.steering.turn_left(50)
                time.sleep(1)
                #장애물 감지 시 4초동안 왼쪽으로 바퀴돌리기
                self.car.steering.turn_right(100)
                time.sleep(0.5)
                print(distance)
                # print(list1)
                self.car.steering.turn_right(130)
                time.sleep(1.9)
                count += 1
                print(count)
                break
           




if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
