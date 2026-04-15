import time
from time import sleep
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

kit.servo[3].angle = 0
#kit.continuous_servo[4].throttle = 1
time.sleep(1)
#kit.continuous_servo[4].throttle = -1
time.sleep(1)
kit.servo[3].angle = 180
#kit.continuous_servo[4].throttle = 0

sleep(2)




print("pan to 0")
kit.servo[0].angle = 0
sleep(1)

print("tilt to 0")
kit.servo[3].angle = 0
sleep(1)

print("pan to 90")
kit.servo[0].angle = 90
sleep(1)

print("tilt to 90")
kit.servo[3].angle = 90
sleep(1)

print("pan to 180")
kit.servo[0].angle = 180
sleep(1)

print("tilt to 180")
kit.servo[3].angle = 180
sleep(1)
