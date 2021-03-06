#!/bin/bash

# Charge le fichier init-photo et execute les commandes initNeededFiles et launchPtoto
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
source ${INIT_SCRIPT}

waitForServer 

cat > ${SESSION_CONFIG} <<EOF
    CHEMIN=$(date +"image-%y-%m-%d_%Hh%Mm%S")
    DOSSIER="${DOSSIER_PREFIX}\${CHEMIN}"
    if test -d "${CLEUSB_PREFIX}"; then
        echo "SDcard ${CLEUSB_PREFIX} exists"
        CLEUSB="${CLEUSB_PREFIX}/session\${CHEMIN}"
    else
        echo "SDcard ${CLEUSB_PREFIX} missing, skipped"
        CLEUSB=none
    fi
    LOG_FILE="${DOSSIER_PREFIX}\${CHEMIN}/photo.log"
EOF


source ${SESSION_CONFIG}

# Initialise les dossiers et fichiers
initNeededFiles

# Lance le client sur le serveur
launchPhoto 0  &

#while sleep 10; do
#     mosquitto_pub -h 192.168.66.5 -t 'ballon/cmd' -m 'sequence'
#done
