import time
import RPi.GPIO as gp
import os

gp.setwarnings(False)
gp.setmode(gp.BOARD)

gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)

gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

def main():
    for i in range(3):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        capture(1,i)

        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        capture(2,i)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        capture(3,i)

        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        capture(4,i)

def capture(cam,i):
    cmd = str("raspistill -t 100 -o camera{0}_{1}.jpg".format(cam,i))
    os.system(cmd)

if __name__ == "__main__":
    main()

    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)