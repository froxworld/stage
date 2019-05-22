import paho.mqtt.client as mqtt #import du client mqtt
import time # pour affichier notre heure

# methode de login au raapartiteur (client, userdata, level, buf)
def on_log(client, donnee, niveau, tampon):
    print("login:"+ tampon)

#methode quand le client va se connecter
def on_connect(client, donnee, drapeaux, resultat_de_connection):
    if resultat_de_connection==0:
        print("{0} connection reussie".format(client))
    else:
        print("probleme de connection code de retour =", resultat_de_connection)

repartiteur = "10.42.0.1"  # adresse du repartiteur (broker)
client = mqtt.Client("python1")  # creation de l'instance d un client
print("connection au broker ", repartiteur)
temps = time.clock()
print (time.clock())

client.on_connect = on_connect
client.on_log = on_log



client.connect(repartiteur)  # connection au repartiteur
time.sleep(4)
client.disconnect() # deconnection
temps = temps - time.clock()
print('le client {0} est deconecter et est rester {1}'.format(client, temps))





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

