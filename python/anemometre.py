# francois auxietre conversion analogique en python 3 pour la lecture d'un anémometre

# pip install pyserial

# The anemometer is designed to output voltage between 0.4V and 2V.
# A value of 0.4V represents no wind and 2V represents a wind speed of 32.4 m/s.
# The relationship between voltage and wind speed is linear,
# meaning that each increase of 0.1V represents an increase of 2.025 m/s in wind speed.

from serial import *
import time

# sensorPin = A0  # pin de branchement
valeurLue = 0  # valeur lue par le cable bleu (entree analogique de l anemometre)
voltage = 0  # valeur en volt lue
conversion = .004882814  # constante de conversion de l'analogique à la valeur reelle 0v à 5v à 0 jusqu' à 1023
attente_mesure = 1000  # temps attente entre deux mesure en ms (1 seconde)
voltageMin = .4  # Mininum de voltage de l'anemometre
voltageMax = 2.0  # Maximum de voltage de l'anemometre
vitesse_vent = 0  # vitesse du vent convertie en m/s
vitesse_vent_minimum = 0
vitesse_vent_maximum = 32
temps = 2  # temps de pause avan la prochiane lecture du senseur

# Module de lecture/ecriture du port série
# Port série ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
with Serial(port="/dev/ttyACM0", baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
    if port_serie.isOpen():
        while True:
            ligne = port_serie.read_line()
            print ligne

nombre = input("Entrez un nombre : ")
port_serie.write(nombre.encode('ascii'))

voltage = valeurLue * conversion  # conversion du voltage

if (voltage < voltageMin):
    vitesse_vent = 0
else:
    vitesse_vent = (voltage - voltageMin) * vitesse_vent_maximum / (
                voltageMax - voltageMin);  # calcul de la vitesse du vent

print("Voltage: ")
Serial.print(voltage)
Serial.print("\t")
Serial.print("Vitesse du vent: ")
Serial.println(vitesse_vent)

time.sleep(temps)
