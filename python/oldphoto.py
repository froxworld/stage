#Francois Auxietre mail:froxworld@gmail.com
#prise de photos pour 3 cameras
# documentation https://pythonhosted.org/RPIO/
# 4 5 6 

import RPi.GPIO as gp
import os, sys
import datetime
import socket
from time import sleep

import paho.mqtt.client as mqtt  # import du client mqtt
from time import gmtime, strftime  # pour affichier notre heure
import time

if len(sys.argv) != 6:
   print("Usage: {0} <repertoire destination> <repertoire SDCARD> <nb photos> <ID du PI> <camera count> ".format(sys.argv[0]))
   sys.exit(1)

destDir = sys.argv[1]
sdDir = sys.argv[2]
nombrePhotos = int(sys.argv[3])
cameraID = int(sys.argv[4])
cameraCount = int(sys.argv[5])

if cameraCount < 1 or cameraCount > 4:
   print("{0}: cameraCount incorrect (entre 1 et 4)".format(sys.argv[0]))
   sys.exit(1)

if cameraID > cameraCount:
   print("{0}: CameraID incorrect (entre 0 et nbre de camera)".format(sys.argv[0]))
   sys.exit(1)

id_client = '1'
mqtt_server = '192.168.66.5'

def getMachineName():
   ipadd = socket.gethostbyname(socket.gethostname())
   return 'pi_' + ipadd.replace('.','_')

class Photo():
   iso = 100
   temps = 100
   exposition = 'auto'
   #preview = '--preview 500:300:500:300'
   preview = '--nopreview'

   cams=(
      (False, False, True),   ## OFF
      (False, False, True), ## CAM 1
      (True,  False, True),  ## CAM 2
      (False, True,  False), ## CAM 3
      (True,  True,  False)   ## CAM 4
   )

   def __init__(self, destDir, sdDir):
      self.indexPhoto = 0
      self.destDir = destDir
      self.sdDir = sdDir
      self.initHard()

   @staticmethod
   def initHard():
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

   def setCam(self, camid):
      gp.output(7,  self.cams[camid][0])
      gp.output(11, self.cams[camid][1])
      gp.output(12, self.cams[camid][2])

   # methode de capture des images
   def capture(self, cam):
    nom = self.destDir + '/camera{0}_{1}.jpg'.format(cam, self.indexPhoto)
    self.indexPhoto += 1

    # deuxieme essai avec des parametre non de base
    # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
    # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
    # -e encoding jpg, -x exiff information dans la photo directement
    # -awb sun cloud  pour deux type de temps pour prendre les photos
    # cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 500 -o {0}{1}{2} -e jpg -x WhiteBalance -x GPS.GPSLatitude={3} -x GPS.GPSLongitude={4} -x GPS.GPSAltitude={5}'.format()

    if self.indexPhoto == 1:
       cmdImage = 'raspistill {0} -ISO {1} -br auto  -awb auto --raw -ex {2} -a 12 -q 100 -t {3} -o {4} -e jpg'.format(self.preview, self.iso, self.exposition, self.temps, nom)
    else:
       cmdImage = 'raspistill {0} -e jpg -o {1} -t {2}'.format(self.preview, nom, self.temps)
    print(cmdImage)
    os.system(cmdImage)
    cmdCle ='cp {0} {1}'.format(nom, self.sdDir)
    os.system(cmdCle)

   def snapAll(self):
        self.setCam(1)
	#lancement de la prise de capture d'image pour la camera 4
        self.capture((self.cameraID*self.cameraCount))

        self.setCam(2)
	#idem pour la 5  ( au milieu)
        self.capture((self.cameraID*self.cameraCount)+1)

        self.setCam(3)
	#idem pour la 6
        self.capture((self.cameraID*self.cameraCount)+2)

        #gp.output(7, True)
        #gp.output(11, True)
        #gp.output(12, False)
        #capture(4,i)
        # temporisation de deux secondes avant de reprendre des photos
        #sleep(2)
        #iso = iso+1

   def __del__(self):
      #fermeture des ports pour eviter les bugs en relançant une autre fois le programme
      self.setCam(0)
      
    
class MqttCmd():

   def __init__(self, id_client, server, photo):
      self.id_client = id_client
      self.photo = photo
      self.repartiteur = server  # adresse du repartiteur (broker)
      self.client = mqtt.Client(id_client)  # creation de l'instance d un client
      print("connection au repartiteur (broker) ", self.repartiteur)
      self.temps = time.clock()
      self.over = False

      self.client.cmd = self
      self.client.on_connect = self.on_connect
      self.client.on_disconnect = self.on_disconect
      self.client.on_log = self.on_log  # comme la methode on log ne retourne rien on enleve les () a premiere vue
      self.client.on_message = self.on_message  # quand on fait un sucribe la ppel de la methode on_message est apellee

      self.client.connect(self.repartiteur)  # connection au repartiteur
      self.client.loop_start()  # debut de la boucle
    
      #  publication de donnee "topic", "contenu du topic "
      date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
      self.client.publish("ballon/clients".format(id_client), "{0}".format(id_client))
      self.client.publish("ballon/{0}/date".format(id_client), "{0}".format(date))
      #self.client.publish("date", "{0}".format(date))
      #self.client.publish("heure/1", "{0}".format(self.temps))
      #self.client.publish("heure/2", "{0}".format(self.temps))

      self.client.subscribe("ballon/{0}/cmd/#".format(id_client))

   def close(self):
      self.client.publish("ballon/close".format(self.id_client), "{0}".format(self.id_client))
      self.client.loop_stop()  # finb de la boucle
      self.client.disconnect()  # deconnection

   @staticmethod
   def on_log(client, donnee, niveau, tampon):
      print("log : Etat du client: " + tampon)

   # methode quand le client va se connecter
   @staticmethod
   def on_connect(le_client, donnee, drapeaux, resultat_de_connection):
      if resultat_de_connection == 0:
         print("connection reussie avec le client :".format(le_client))
      else:
         print("probleme de connection code de retour =", resultat_de_connection)

   # methode au moment de la deconnection
   @staticmethod
   def on_disconect(le_client, donnee, drapeaux, resultat_de_connection=0):
      print("Deconnection du client avec le code de retour ", resultat_de_connection)
    
   # derniere methode on_message quand le client a souscrit
   @staticmethod
   def on_message(le_client, donnee, message):
      self = le_client.cmd
      sujet = message.topic
      cmd = message.payload.decode("utf-8")
      print("message: {0}/{1} {2}".format(message.topic, cmd, str(self)))
      if cmd == 'stop':
         self.client.publish("ballon/{0}/status".format(id_client), "stop received")
         self.over = True
         self.close()
      elif cmd == 'sequence':
         self.client.publish("ballon/{0}/status".format(id_client), "snap received")
         self.photo.snapAll()
         self.client.publish("ballon/{0}/status".format(id_client), "snap {0} done".format(self.photo.indexPhoto))

   def __str__(self):
      return "MqttClient {0}".format(self.id_client)

#programme principal  pour la capture des images
def main():
   photo = Photo(destDir, sdDir)
   mqtt = MqttCmd(getMachineName(), mqtt_server, photo)

   if nombrePhotos > 0:
      for i in range(nombrePhotos):
         photo.snapAll()
   else:
      while not mqtt.over:
         sleep(1)

if __name__ == "__main__":
    main()
