from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.capture('/home/pi/francois/stage/python/image1.jpg')
