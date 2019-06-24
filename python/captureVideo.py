import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording('home/pi/francois/stage/video/foo.h264')
    time.sleep(0.2)
    camera.stop_recording()
    camera.stop_preview()






#camera = picamera.PiCamera()
#try:
#    camera.start_preview()
#    time.sleep(10)
#    camera.stop_preview()
#finally:
#    camera.close()

#camera.start_recording('/home/pi/francois/stage/video/video.avi')

