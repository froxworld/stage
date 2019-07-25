#Francois Auxietre mail:froxworld@gmail.com
#prise de photos pour 3 cameras
# documentation https://pythonhosted.org/RPIO/

# from picamera import PiCamera
from time import sleep
import json  # pour sauvegarder  les coordonnees de chaque fichier

# import cv2
import time



import RPi.GPIO as gp
import os
from time import sleep


numero = 0
latitude = 10
longitude = 10
altitude = 50
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
meteo = 0  # 0 soleil pour un iso 200
# 1 nuageux pour un iso 800

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
    'nom_fichier_image': nomFichierImage,
    'meteo': meteo
}

# desactivation des warnings
gp.setwarnings(False)  # pour acceder au cameras avec les pin 7 11 12
gp.setmode(gp.BOARD)  # initialisation des pin pour 4 cameras

#configuration des ports 7,11,12, 15, 16, 21, 22
gp.setup(7, gp.OUT)  # setup
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


# camera = PiCamera()  # pour prendre une photo avec picamera plustoto que raspistill

def main():
    for index in range(3):
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        # lancement de la prise de capture d'image pour la camera 4
        capture(4, index, meteo)

        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        # lancement de la prise de capture d'image pour la camera 4
        capture(5, index, meteo)

        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        # lancement de la prise de capture d'image pour la camera 4
        capture(6, index, meteo)

        # en cas de quatrieme camera
        #gp.output(7, True)
        #gp.output(11, True)
        #gp.output(12, False)
        #capture(4, index, meteo)
        # temporisation de deux secondes avant de reprendre des photos
        sleep(2)

        # sauvegarde des informations sous format json de toutes les photos, gps, ...
        with open('data.txt', 'w') as fichierjson:
            json.dump(information, fichierjson)  # fermeture du fichier automatique avec with


def capture(camera, index, meteo):
    cmd = str("raspistill -t 100 -o camera{0}_{1}.jpg".format(camera, index))
    # deuxieme essai avec des parametre non de base
    # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
    # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
    # -e encoding jpg, -x exiff information dans la photo directement
    # -awb sun cloud  pour deux type de temps pour prendre les photos

    cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 500 -o {0}{1}{2} -e jpg -x WhiteBalance -x GPS.GPSLatitude={3} -x GPS.GPSLongitude={4} -x GPS.GPSAltitude={5}'.format(
     '/home/pi/francois/stage/image/camera1-', index, '.jpg', latitude, longitude, altitude)
    os.system(cmd)


if __name__ == "__main__":
    main()
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)