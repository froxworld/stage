#!/bin/bash

# Configuration
DOSSIER_PREFIX="/home/pi/"
INIT_SCRIPT=/home/pi/stage/python/init-photo.sh
APPLICATION=/home/pi/stage/python/photo.py
SESSION_CONFIG=/home/pi/session-config.sh
SDCARD_LOCATION=/media/pi/CLEUSB
SDCARD_PREFIX=${SDCARD_LOCATION}/image
NB_PHOTOS=0
NB_CAMERA=3

# Installation

initNeededFiles() {
    sleep 10

    if test -d "${SDCARD_LOCATION}"; then
	test -d "${SDCARD_PREFIX}" || sudo mkdir -p "${SDCARD_PREFIX}"
	test -d "${SDCARD}"        || sudo mkdir -p "${SDCARD}"
	sudo chmod -R 777  ${SDCARD}
    else
	SDCARD=none
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
    while sleep 1; do
	python3 "${APPLICATION}" "${DOSSIER}" "${SDCARD}" "${NB_PHOTOS}" ${PI_ID} "${NB_CAMERA}" 2>&1 > ${LOG_FILE}.${PI_ID}
	syncClientFiles
    done
}
