#!/bin/bash
cd "$(dirname "$0")"
# Installa Pytube
pip3 install pytube
clear
python3 main.py
read -p "Premi INVIO per chiudere..."
