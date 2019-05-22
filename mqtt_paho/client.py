import paho.mqtt.client as mqtt


# The callback for when the client receives a CONNACK response from the server.

def on_connect(client, userdata, flags, resutat_de_conection):
    #
    print("connection reussie  "+str(resutat_de_conection))

    # Subscribing in on_connect() means that if we lose the connection and

    # reception de tous les messages
    # client.subscribe("$SYS/#")
    #client.sucribe("sensors/#")
    client.sucribe([("sensors/#", 0), ("sensors/temperature",2)])


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
