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
lattitude = 0
longitude = 0

if cameraCount < 1 or cameraCount > 4:
   print("{0}: cameraCount incorrect (entre 1 et 4)".format(sys.argv[0]))
   sys.exit(1)

id_client = '1'
mqtt_server = '192.168.66.5'

def getMachineName():
   #ipadd = socket.gethostbyname(socket.gethostname())
   #return 'pi_' + ipadd.replace('.','_')
   return socket.gethostname()

class Photo():
   iso = 100
   temps = 1
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
   #initilisation des repertoires nombre de cameras repertoire de destination et repertoire de la cleUsb
   def __init__(self, cameraCount, destDir, sdDir):
      self.indexPhoto = 0
      self.destDir = destDir
      self.sdDir = sdDir
      self.cameraCount = cameraCount
      self.initHard()

   #mise en place du multiplexeur des cameras et des Gpio
   def initHard(self):
      if self.cameraCount > 1:
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
      if self.cameraCount > 1:
         gp.output(7,  self.cams[camid][0])
         gp.output(11, self.cams[camid][1])
         gp.output(12, self.cams[camid][2])

   # methode de capture des images
   def capture(self, index, cam):
    global lattitude, longitude
    basename = self.destDir + '/photo-{0}_cam-{1}'.format(index, cam)
    nom = basename + '.jpg'
    jsonName = basename + '.json'

    # deuxieme essai avec des parametre non de base
    # reglages iso 200, awb balance des blancs auto, ex exposition auto , -a heure et date 20:09:33 10/12/2019
    # -q qualite 100 , -o output chemin de sortie, -r raw fichier non compresser, -t time une photo toute les 2 secondes
    # -e encoding jpg, -x exiff information dans la photo directement
    # -awb sun cloud  pour deux type de temps pour prendre les photos
    # cmd = 'raspistill -ISO 200 -awb auto -ex auto -a 12 -q 100 -t 500 -o {0}{1}{2} -e jpg -x WhiteBalance -x GPS.GPSLatitude={3} -x GPS.GPSLongitude={4} -x GPS.GPSAltitude={5}'.format()

    if self.indexPhoto == 1:
       cmdImage = 'raspistill {0} -x time={3} -ISO {1} -br auto  -awb auto --raw -ex {2} -a 12 -q 100 -t {3} -o {4} -e jpg'.format(self.preview, self.iso, self.exposition, self.temps, nom)
    else:
       cmdImage = 'raspistill {0} -x time={2} -e jpg -o {1} -t {2}'.format(self.preview, nom, self.temps)
    print(cmdImage)
    os.system(cmdImage)

    jsonFile = open(jsonName, "w+")
    jsonName.write('{ "name":"{0}", "lat":"{1}", "long":"{2}" }'.format(basename, lattitude, longitude))
    jsonName.close()

    if self.sdDir != "none":
       cmdCle ='cp {0} {1}'.format(nom, self.sdDir)
       os.system(cmdCle)

   # methode de capture des images
   def record(self, index):
    nom = self.destDir + '/video-{0}.jpg'.format(index)
    cmdImage = 'raspivid -o {0} -t 20000 '.format(nom)
    print(cmdImage)
    os.system(cmdImage)

    if self.sdDir != "none":
       cmdCle ='cp {0} {1}'.format(nom, self.sdDir)
       os.system(cmdCle)

   def snapTime(self, time):
      self.temps  = time

   def snapAll(self, index):
      print('snap prend des photo ({0})'.format(index))
      if index == -1:
         index = self.indexPhoto

      self.setCam(1)
      self.capture(index, (cameraID*self.cameraCount))

      if self.cameraCount > 1:
        self.setCam(2)
        self.capture(index, (cameraID*self.cameraCount)+1)

      if self.cameraCount > 2:
        self.setCam(3)
        self.capture(index, (cameraID*self.cameraCount)+2)

      if self.cameraCount > 3:
        self.setCam(4)
        self.capture(index, (cameraID*self.cameraCount)+3)

      self.indexPhoto += 1

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
      print("log : Serveur demarré")
    
      #  publication de donnee "topic", "message "
      date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
      print("ballon/clients{0}".format(self.id_client), "ballon/{0}/date".format(self.id_client))
      self.client.publish("ballon/status",  "{0}".format(self.id_client))
      self.client.publish("ballon/{0}/status".format(self.id_client),  "client:{0} repertoire:{1}".format(self.id_client, self.photo.destDir))
      self.client.publish("ballon/{0}/status".format(self.id_client),  "{0}".format(date))

      # Ecoute spécifique d'un client
      self.client.subscribe("ballon/{0}/cmd/#".format(self.id_client))

      # Ecoute sur un canal commun à tous les clients.
      self.client.subscribe("ballon/cmd")

      # Ecoute sur un des GPS.
      self.client.subscribe("ballon/gps")

   def close(self):
      self.client.publish("ballon/close".format(self.id_client), "{0}".format(self.id_client))
      self.client.loop_stop()  # fin de la boucle
      self.client.disconnect()  # deconnection

   @staticmethod
   def on_log(client, donnee, niveau, tampon):
      print("log : Etat du client: " + tampon)

   # methode quand le client va se connecter
   @staticmethod
   def on_connect(le_client, donnee, drapeaux, resultat_de_connection):
      if resultat_de_connection == 0:
         print("connection reussie avec le client :{0}".format(le_client))
      else:
         print("probleme de connection code de retour =", resultat_de_connection)

   # methode au moment de la deconnection
   @staticmethod
   def on_disconect(le_client, donnee, drapeaux, resultat_de_connection=0):
      print("Deconnection du client avec le code de retour ", resultat_de_connection)

   # derniere methode on_message quand le client a souscrit
   @staticmethod
   def on_message(le_client, donnee, message):
      global lattitude, longitude
      self = le_client.cmd
      sujet = message.topic
      toutelacommande = message.payload.decode("utf-8")

      if message.topic == "ballon/gps":
         coordinates = toutelacommande.split(";")
         lattitude = coordinates[0]
         longitude = coordinates[1]

      else:
         cmd = toutelacommande.split("=")
         print("message: {0}/{1} {2}".format(message.topic, cmd, str(self)))
         # en faisant la commnade stop  on arete la prise de vue de photo
         if cmd[0] == 'stop':
            self.client.publish("ballon/{0}/status".format(self.id_client), "arret de reception")
            self.over = True
            self.close()
         # on lance une prise de une photo
         if cmd[0] == 'sequence':
            self.client.publish("ballon/{0}/status".format(self.id_client), "le client :{0} prend la photo{1}".format(self.id_client, self.photo.indexPhoto))
            if len(cmd) == 2:
               self.photo.snapAll(int(cmd[1]))
            else:
               self.photo.snapAll(-1)
            self.client.publish("ballon/{0}/status".format(self.id_client), "photo{0} prise par le client :{1}".format(self.photo.indexPhoto, self.id_client))
         # on peut lancer une prise de vue avec plusieurs photo ex 'photo=20'
         if cmd[0] == 'photo':
            if len(cmd) != 2:
               self.client.publish("ballon/{0}/status".format(self.id_client), "erreur: sur prise de photo N°{0}".format(self.id_client))
            else:
               try:
                  nbPhotos=int(cmd[1])
                  for ind in range(nbPhotos):
                     self.photo.snapAll(-1)
                     self.client.publish("ballon/{0}/status".format(self.id_client), "le client :{0} a déjà fait {1} photo sur les {2}".format(self.id_client, ind+1, nbPhotos))
                  self.client.publish("ballon/{0}/status".format(self.id_client), "le client :{0} a fini ses {1} photos".format(self.id_client, nbPhotos))
               except Exception as e:
                  self.client.publish("ballon/{0}/status".format(self.id_client), "erreur : {1} sur le client :{0},le parametre passé est {2}".format(self.id_client, str(e), cmd[1]))
         # si on veut changer le temps d'attente  avant de prendre une photo
         if cmd[0] == 'time':
            if (len(cmd) == 2):
               timeValue = int(cmd[1])
               self.photo.snapTime(timeValue)
               self.client.publish("ballon/{0}/status".format(self.id_client), "le client :{0} a pris sa photo en {1} secondes".format(self.id_client,timeValue/1000))
         # on peut effacer le repertoire de destination des photos
         if cmd[0] == 'erase':
            os.system("rm -rf {0}".format(self.photo.destDir))
            self.over = True
            self.close()
         # on peut effacer l'ensemble des repertoire contenant des photos
         if cmd[0] == 'eraseAll':
            os.system("rm -rf /home/pi/image-*")
            self.over = True
            self.close()

   def __str__(self):
      return "MqttClient {0}".format(self.id_client)

#programme principal  pour la capture des images
def main():
   photo = Photo(cameraCount, destDir, sdDir)
   mqtt = MqttCmd(getMachineName(), mqtt_server, photo)
   sys.stdout.flush()

   if nombrePhotos > 0:
      for i in range(nombrePhotos):
         photo.snapAll(-1)
         sys.stdout.flush()
   else:
      while not mqtt.over:
         sleep(1)
         sys.stdout.flush()

if __name__ == "__main__":
    main()
