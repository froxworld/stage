from picamera import PiCamera
from time import sleep

camera = PiCamera()
for i in range(5):
	sleep(1)
	camera.capture('/home/pi/francois/stage/image%s.jpg' % i)
