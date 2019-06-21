import numpy as np
import RPi.GPIO as gp
import os
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i1", "--img1", required=True, help="path to first image")
ap.add_argument("-i2", "--img2", required=True, help="path to second image")
args = vars(ap.parse_args())

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.output(11, True)
gp.output(12, True)


def main():
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    capture(1)

    gp.output(7, False)
    gp.output(11, True)
    gp.output(12, False)
    capture(3)

    image1 = cv2.imread(args['img1'])
    image2 = cv2.imread(args['img2'])

def capture(cam):
    if cam == 1:
       cmd = "raspistill -vf -hf -t 1000 -o %s" % args['img1']
    if cam == 3:
       cmd = "raspistill -vf -hf -t 1000 -o %s" % args['img2']       
    os.system(cmd)

if __name__ == "__main__":

    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)

