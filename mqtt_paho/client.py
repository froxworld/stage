import paho.mqtt.client as mqtt  # import du client mqtt
from time import gmtime, strftime  # pour affichier notre heure
from enum import Enum
import time
class Extension(Enum):
    jpg = 1
    png = 2
    svg = 3


id_client = '1'
nom_image = "test"
chemin = "/home/pi/francois/"
id_camera = 0
compteur = 0

# methode de login au raapartiteur (client, userdata, level, buf)
def on_log(client, donnee, niveau, tampon):
    print("log : Etat du client: " + tampon)


# methode quand le client va se connecter
def on_connect(le_client, donnee, drapeaux, resultat_de_connection):
    if resultat_de_connection == 0:
        print("connection reussie avec le client :".format(le_client))
    else:
        print("probleme de connection code de retour =", resultat_de_connection)

# methode au moment de la deconnection
def on_disconect(le_client, donnee, drapeaux, resultat_de_connection):
    print("Deconnection du client ave le code de retour ", resultat_de_connection)

# derniere methode on_message quand le client a souscrit
def on_message(le_client, donnee, message):
    sujet = message.topic
    decodage = str(message.plaload.decode("utf-8", "ignore"))
    print(decodage)


repartiteur = "10.42.0.1"  # adresse du repartiteur (broker)
client = mqtt.Client(id_client)  # creation de l'instance d un client
print("connection au repartiteur (broker) ", repartiteur)
temps = time.clock()

client.on_connect = on_connect  # bizarre en python un appel de methode sans () ?
client.on_disconnect
client.on_log = on_log  #  comme la methode on log ne retourne rien on enleve les () a premiere vue
client.on_message # quand on fait un sucribe la ppel de la methode on_message est apellee

client.connect(repartiteur)  # connection au repartiteur
client.loop_start()  # debut de la boucle

#  publication de donnee "topic", "contenu du topic "
date = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
client.publish("date", "{0}".format(date))
client.publish("heure/1", "{0}".format(temps))
client.publish("heure/2", "{0}".format(temps))

if id_camera == 0:
    # pour les enum on peut faire
    client.publish("camera", "{0}camera/{1}{2}.{3}".format(chemin,nom_image,compteur, Extension.jpg.name))
    compteur = compteur + 1

client.publish("photo", "{0}/photo/{1}.{2}".format(chemin,nom_image, Extension.jpg))

client.publish("video", "video")

# reception d un topic on s'abonne
client.subscribe(("heure/#"))

time.sleep(4)
client.loop_stop()  # finb de la boucle
client.disconnect()  # deconnection
temps_total = int(abs(temps - time.clock()) * 1000)
print('le client {0} est deconecter et est rester {1} secondes'.format(client, temps_total))

'''
# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, resutat_de_conection):
    #
    print("connection reussie  "+str(resutat_de_conection))

    # Subscribing in on_connect() means that if we lose the connection and

    # reception de tous les messages
    # client.subscribe("$SYS/#")
    #client.sucribe("sensors/#")
    client.sucribe([("sensors/#", 0), ("sensors/temperature",2)])
    # mosquitto_sub -h 10.42.0.1 -t sensors/#


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


    message_client = msg.is_published()
    print('message', message_client)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.42.0.1", 1883, 60)

# creation d une boulce infini pour attendre les messages
client.loop_forever()
'''
