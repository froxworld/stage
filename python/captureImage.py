from picamera import PiCamera
from time import sleep
import json #pour sauvegarder  les coordonnees de chaque fichier

int numero=0
fichier_data = open('data.json', 'w')

information={
	'date':'date',
	'numero_camera', numero,
	'position_gps_latitude', latitude,
	'position_gps_longitude', longitude,
	'hauteur', hauteur
	'vitesse_vent', vitesse_vent,
	'angle_de_roulis', roulis,
	'angle_de_tangage', tangage,
	'jour', jour,
	'mois', mois,
	'annee', annee,
	'heure', heure,
	'minute', minute,
	'nom_fichier_image', nomFichierImage,
	

}

camera = PiCamera()
for i in range(5):
	sleep(1)
	camera.capture('/home/pi/francois/stage/image/camera1-image%s.jpg' % i)
	
	
with open('data.txt', 'w') as fichierjson:
	json.dump(information, fichierjson)  #fermeture du fichier automatique avec with 

