from gpiozero import AngularServo
from time import sleep

panservo = AngularServo(18, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)
tiltservo = AngularServo(17, min_angle=0, max_angle=180, min_pulse_width=0.0005, max_pulse_width=0.0025)

while (True):
	print("moving to 90")
	panservo.angle = 0
	tiltservo.angle = 30
	sleep(2)
	print("moving to 0")
	panservo.angle = 90
	tiltservo.angle = 30
	sleep(2)
	print("moving to 180")
	panservo.angle = 180
	tiltservo.angle = 30
	sleep(2)
