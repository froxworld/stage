import gps
import time
import socket

mqtt_server = '192.168.66.5'
gpsd = gps.gps(mode=gps.WATCH_ENABLE)

class MqttCmd():
    def __init__(self, id_client, server):
        self.repartiteur = server  # adresse du repartiteur (broker)
        self.client = mqtt.Client(id_client)  # creation de l'instance d un client
        print("connection au repartiteur (broker) ", self.repartiteur)
        self.over = False
        self.client.connect(self.repartiteur)  # connection au repartiteur
        self.client.loop_start()  # debut de la boucle
        print("log : Serveur demarré")

    def main():
        while True:
            gpsdata = gpsd.next()
            if "lon" in gpsdata:
                latitute =  gpsdata.lon
                longitude = gpsdata.lat
                self.client.publish("ballon/gps",  "{0};{1}".format(latitute, longitude))
                print("gps : { lat:{0}, lon:{1} }".format(latitute, longitude))
            else:
                self.client.publish("ballon/{0}/status".format(socket.gethostname()), "no GPS")
                print("gps : pas de position")
            time.sleep(1)
            
mqtt = MqttCmd(socket.gethostname() + '_gps', mqtt_server)




# LM -- import sys
# LM -- import serial
# LM -- import math
# LM -- import operator
# LM -- import time
# LM -- import socket
# LM -- 
# LM -- GPS_IP = "127.0.0.3"
# LM -- GPS_PORT = 5005
# LM -- 
# LM -- t_gps = 0
# LM -- t_fail = 0.0
# LM -- t_print = time.time()
# LM -- 
# LM -- ser = serial.Serial('/dev/ttyUSB1', 4800, timeout=1)
# LM -- 
# LM -- while True:
# LM -- 
# LM --     hack = time.time()
# LM -- 
# LM --     gps_raw = ser.readline()
# LM --     if "*" in gps_raw:
# LM --         gps_split = gps_raw.split('*')
# LM --         gps_sentence = gps_split[0].strip('$')
# LM --         cs0 = gps_split[1][:-2]
# LM --         cs1 = format(reduce(operator.xor, map(ord, gps_sentence), 0), 'X')
# LM --         if len(cs1) == 1:
# LM --             cs1 = "0" + cs1
# LM --         if cs0 == cs1:
# LM -- 
# LM --             gps_vars = gps_sentence.split(',')
# LM --             title = gps_vars[0]
# LM -- 
# LM --             if title == "GPRMC":
# LM --                 t_fail = 0.0
# LM --                 t_gps = hack
# LM --                 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# LM --                 sock.sendto(gps_raw, (GPS_IP, GPS_PORT))
# LM -- 
# LM --     if (hack - t_gps) > 10.0:
# LM --         if (hack - t_print) > 1.0:
# LM --             t_fail += 1.0
# LM --             gps_sentence = "IIXDR,GPS_FAIL," + str(round(t_fail / 60, 1))
# LM --             cs = format(reduce(operator.xor, map(ord, gps_sentence), 0), 'X')
# LM --             if len(cs) == 1:
# LM --                 cs = "0" + cs
# LM --             gps_sentence = "$" + gps_sentence + "*" + cs
# LM --             sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# LM --             sock.sendto(gps_sentence, (GPS_IP, GPS_PORT))
# LM --             t_gps = hack
