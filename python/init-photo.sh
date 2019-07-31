#!/bin/bash

# Configuration
DOSSIER_PREFIX="/home/pi/"
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
APPLICATION=/home/pi/stage/python/photo.py
SESSION_CONFIG=/home/pi/session-config.sh
CLEUSB_LOCATION=/media/pi/CLEUSB
CLEUSB_PREFIX=${CLEUSB_LOCATION}/image
NB_PHOTOS=0   #si le nombre de photo = 0 alors on passe en Mqtt de photo.py
NB_CAMERA=3
# CLEUSB = /home/pi/

# Installation

initNeededFiles() {
    sleep 10

    if test -d "${CLEUSB_LOCATION}"; then
	test -d "${CLEUSB_PREFIX}" || sudo mkdir -p "${CLEUSB_PREFIX}"
	test -d "${CLEUSB}"        || sudo mkdir -p "${CLEUSB}"
	sudo chmod -R 777  ${CLEUSB}    #CLEUSB non définie
    else
	CLEUSB=none
    fi

    test -d "${DOSSIER}" || mkdir -p ${DOSSIER}
}

waitForServer() {
    while ! ping -c 1 192.168.66.5; do
	sleep 1
    done
}

syncClientFiles() {
    scp ballonserver:${SESSION_CONFIG} ${SESSION_CONFIG}
    scp ballonserver:${INIT_SCRIPT} ${INIT_SCRIPT}
    scp ballonserver:${APPLICATION} ${APPLICATION}
}

syncPhotoOnServer() {
    (
	while sleep 5; do
	    rsync -auv "${DOSSIER}" ballonserver:${DOSSIER_PREFIX}
	done
    ) 2>&1 > /dev/null &
}

syncDateTimeFromServer() {
    sudo date -s "$(ssh ballonserver date --rfc-3339=ns )"
}

launchPhoto() {
    local PI_ID="$1"

    # Boucle de lancement automatique du client MQTT pour
    #  pour prendre des photos en cas d'erreur (s'il quitte)
    while sleep 1; do
	python3 "${APPLICATION}" "${DOSSIER}" "${CLEUSB}" "${NB_PHOTOS}" ${PI_ID} "${NB_CAMERA}" 2>&1 > ${LOG_FILE}.${PI_ID}
        syncClientFiles
    done
}
