#Francois Auxietre mail:froxworld@gmail.com
#prise de photos pour 3 cameras
# documentation https://pythonhosted.org/RPIO/
# 4 5 6 

import RPi.GPIO as gp
import os, sys
from time import sleep
import datetime
import numpy as np


iso = 100
nombrePhotos = 2
temps = 2000
exposition = 'auto'
raw = '--raw'
preview = '--preview 500:300:500:300'
#camera1 = 1
#camera2 = 2
#camera3 = 3
camera1 = 4
camera2 = 5
camera3 = 6
#camera1 = 7
#camera2 = 8
#camera3 = 9






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
   sleep(8)
   for i in range(nombrePhotos):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
	#lancement de la prise de capture d'image pour la camera 4
        capture(camera1,i,temps)

        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
	#idem pour la 5  ( au milieu)
        capture(camera2,i,temps)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
	#idem pour la 6
        capture(camera3,i,temps)


        #gp.output(7, True)
        #gp.output(11, True)
        #gp.output(12, False)
        #capture(4,i)
        # temporisation de deux secondes avant de reprendre des photos
        #sleep(2)
        #iso = iso+1

# methode de capture des images
def capture(cam,i,temps):
    pathCle = "/media/pi/CLEUSB/"
    pathImage = ""
    #if not os.path.isdir(path):
    #     os.mkdir(path)
    nom = 'camera{0}{1}{2}{3}{4}{5}'.format(cam,'_',i,'_temps_',temps,'.jpg')
    print(nom)
    cmdImage = 'raspistill -ISO {0} {12} -br auto  -awb auto -ex {10} -a 12 -q 100 -t {9} -o {1}{2}{3}{4}{5}{6}{7}{8}  -e jpg'.format(iso,pathImage ,'camera', cam, '_',  i,'_temps_',temps,'.jpg', temps, exposition, raw, preview)
    #print(cmd)
    #cmd = str("raspistill -vf - hf -t 100 -o camera{0}_{1}.jpg".format(cam,i))
    os.system('pwd')

    os.system(cmdImage)
    cmdCle ='cp {0} /media/pi/CLEUSB'.format(nom)
    os.system(cmdCle)

if __name__ == "__main__":
    main()
    #fermeture des ports pour eviter les bugs en relançant une autre fois le programme
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
