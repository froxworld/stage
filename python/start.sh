#!/bin/bash
cd /home/pi
date heure linux bash
CHEMIN=$(date +"-%d-%m-%y-%H-%M-%S")
IMAGE="image"
DOSSIER="$IMAGE$CHEMIN"
mkdir $DOSSIER
cp photo.py /home/pi/$DOSSIER
cd $DOSSIER
python3 photo.py
