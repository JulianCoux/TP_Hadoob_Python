#!/usr/bin/env python3

import sys
from country import init_pays, getCountryAt

# Lecture du fichier d'entrée ligne par ligne
for line in sys.stdin:
    fields = line.strip().split('\t')
    try:
        # Extraire longitude et latitude
        longitude = float(fields[10])  # Longitude est en 11ème position (index 10)
        latitude = float(fields[11])   # Latitude est en 12ème position (index 11)

        init_pays()
        countryCode = getCountryAt(latitude, longitude)

        # print("Longitude:", longitude," Latitude:", latitude)
        if countryCode != "":
            print(countryCode, "1")

    except ValueError:
        # Si les données sont mal formatées ou manquantes
        print("Données manquantes ou mal formatées pour cette ligne.")
        continue
