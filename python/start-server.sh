#!/bin/bash

# Charge le fichier et execute les commandes
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
source ${INIT_SCRIPT}

cat > ${SESSION_CONFIG} <<EOF
    CHEMIN=$(date +"image-%d-%m-%y-%H-%M-%S")
    DOSSIER="${DOSSIER_PREFIX}\${CHEMIN}"
    SDCARD="${SDCARD_PREFIX}/session\${CHEMIN}"
    LOG_FILE="${DOSSIER_PREFIX}\${CHEMIN}/photo.log"
EOF


source ${SESSION_CONFIG}

# Initialise les dossiers et fichiers
initNeededFiles

# Lance le client sur le serveur
launchPhoto 1
