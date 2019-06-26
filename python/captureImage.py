from picamera import PiCamera
from time import sleep
import json  # pour sauvegarder  les coordonnees de chaque fichier

import numpy as np
import RPi.GPIO as gp
import os
import argparse
import cv2

numero = 0
latitude = 0
longitude = 0
hauteur = 0
vitesse_vent = 0
roulis = 0
tangage = 0
jour = 'lundi'
annee = 2019
mois = 'juin'
heure = 0
minute = 0
nomFichierImage = 'raspberry{0}'.format(numero)
meteo = 'soleil' #soleil nuageux

information = {
    'date': 'date',
    'numero_camera': numero,
    'position_gps_latitude': latitude,
    'position_gps_longitude': longitude,
    'hauteur': hauteur,
    'vitesse_vent': vitesse_vent,
    'angle_de_roulis': roulis,
    'angle_de_tangage': tangage,
    'jour': jour,
    'mois': mois,
    'annee': annee,
    'heure': heure,
    'minute': minute,
    'nom_fichier_image': nomFichierImage
}

gp.setwarnings(False)  # pour acceder au cameras avec les pin 7 11 12
gp.setmode(gp.BOARD)
gp.setup(7, gp.OUT)
gp.setup(11, gp.OUT)
gp.setup(12, gp.OUT)
camera = PiCamera()


def main():
    for index in range(3):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        capture(1, index, meteo)

        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        capture(2, index, meteo)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        capture(3, index, meteo)

        # sauvegarde des informations sous format json de toutes les photos, gps, ...
        with open('data.txt', 'w') as fichierjson:
            json.dump(information, fichierjson)  # fermeture du fichier automatique avec with


def capture(numeroCamera, index, meteo):


    # -awb sun cloud  pour deux type de temps pour prendre les photos


    if numeroCamera == 1:
        # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
        # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
        # -e encoding jpg, -x exiff information dans la photo directement
        cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 2000 -o {0}{1}{2} -e jpg --exif WhiteBalance, GPSLatitude, GPSLongitude, GPSAltitude, GPSAreaInformation,'.format(
            '/home/pi/francois/stage/image/camera', index, '.jpg')
        camera.capture('/home/pi/francois/stage/image/camera1-image%s.jpg' % index)
        os.system(cmd)

    if numeroCamera == 2:
        # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
        # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
        # -e encoding jpg, -x exiff information dans la photo directement
        cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 2000 -o {0}{1}{2} -e jpg --exif WhiteBalance, GPSLatitude, GPSLongitude, GPSAltitude, GPSAreaInformation,'.format(
            '/home/pi/francois/stage/image/camera', index, '.jpg')
        camera.capture('/home/pi/francois/stage/image/camera2-image%s.jpg' % index)
        os.system(cmd)

    if numeroCamera == 3:
        # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
        # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
        # -e encoding jpg, -x exiff information dans la photo directement
        cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 2000 -o {0}{1}{2} -e jpg --exif WhiteBalance, GPSLatitude, GPSLongitude, GPSAltitude, GPSAreaInformation,'.format(
            '/home/pi/francois/stage/image/camera', index, '.jpg')
        camera.capture('/home/pi/francois/stage/image/camera3-image%s.jpg' % index)
        os.system(cmd)


if __name__ == "__main__":
    main()

# fichier_data = open('data.json', 'w')
