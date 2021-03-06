#Francois Auxietre mail:froxworld@gmail.com
#prise de photos pour 3 cameras
# documentation https://pythonhosted.org/RPIO/

import RPi.GPIO as gp
import os
from time import sleep


# desactivation des warnings
gp.setwarnings(False)
gp.setmode(gp.BOARD)

#configuration des ports 7,11,12, 15, 16, 21, 22
gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)
gp.setup(15, gp.OUT)
gp.setup(16, gp.OUT)
gp.setup(21, gp.OUT)
gp.setup(22, gp.OUT)

#configuration des sorties
gp.output(11, True)
gp.output(12, True)
gp.output(15, True)
gp.output(16, True)
gp.output(21, True)
gp.output(22, True)

#programme principal  pour la capture des images
def main():
    for i in range(5):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        #lancement de la prise de capture d'image pour la camera 4
        capture(4,i)

        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        #idem pour la 5  ( au milieu)
        capture(5,i)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        #idem pour la 6
        capture(6,i)


        #gp.output(7, True)
        #gp.output(11, True)
        #gp.output(12, False)
        #capture(4,i)
        # temporisation de deux secondes avant de reprendre des photos
        sleep(2)

# methode de capture des images
def capture(cam,i):
    cmd = str("raspistill -vf -hf -t 100 -o camera{0}_{1}.jpg".format(cam,i))
    os.system(cmd)

if __name__ == "__main__":
    main()
    #fermeture des ports pour eviter les bugs en relançant une autre fois le programme
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
