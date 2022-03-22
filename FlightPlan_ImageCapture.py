from djitellopy import Tello
from time import sleep
import cv2
global img

tello = Tello()

tello.connect()
print(tello.get_battery())

#take off 6 feet
tello.takeoff()
tello.move_up(91)
sleep(2)

#fly forward 116 feet
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(250)
sleep(2)

#turn towards cafeteria
tello.rotate_counter_clockwise(65)
sleep(2)

tello.streamon()
frame_read = tello.get_frame_read()

#photo
cv2.imwrite("picture.png", frame_read.frame)

#turn to library
tello.rotate_counter_clockwise(115)
sleep(2)

#fly forward 116 feet
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(500)
sleep(.5)
tello.move_forward(250)
sleep(2)

#move up to middle school library
tello.move_up(500)
sleep(.5)

#turn towards library
tello.rotate_counter_clockwise(115)

#take photo
cv2.imwrite("picture2.png", frame_read.frame)

tello.flip_forward()
tello.land()
tello.end()
