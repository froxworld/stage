#!/bin/bash

# Charge le fichier et execute les commandes
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
source ${INIT_SCRIPT}

waitForServer 

cat > ${SESSION_CONFIG} <<EOF
    CHEMIN=$(date +"image-%d-%m-%y-%H-%M-%S")
    DOSSIER="${DOSSIER_PREFIX}\${CHEMIN}"
    if test -d "${SDCARD_PREFIX}"; then
        echo "SDcard ${SDCARD_PREFIX} exists"
        SDCARD="${SDCARD_PREFIX}/session\${CHEMIN}"
    else
        echo "SDcard ${SDCARD_PREFIX} missing, skipped"
        SDCARD=none
    fi
    LOG_FILE="${DOSSIER_PREFIX}\${CHEMIN}/photo.log"
EOF


source ${SESSION_CONFIG}

# Initialise les dossiers et fichiers
initNeededFiles

# Lance le client sur le serveur
launchPhoto 1 &

while sleep 10; done

      mosquito_pub -h 192.168.66.5 -t 'ballon/cmd' -m 'sequence'

done
