#!/bin/bash

# Charge le fichier et execute les commandes
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
source ${INIT_SCRIPT}

# Attends le serveur
waitForServer

# Met a jour la date (en gros à 1s près)
syncDateTimeFromServer

# Synchronise les fichiers de configuration
syncClientFiles
source ${INIT_SCRIPT}
source ${SESSION_CONFIG}

# Initialise les dossiers et fichiers
initNeededFiles

# Synchronise les fichiers image en arrière plan
syncPhotoOnServer 2

# Lance un programme qui surveille le GPS et publie la position avec MQTT sur ballon/gps
python ${DOSSIER_GIT}/gps.py &

# Lance le client sur le serveur
launchPhoto 2
