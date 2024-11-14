#!/usr/bin/env python3

import sys

# Lecture du fichier d'entrée ligne par ligne
for line in sys.stdin:
    # Suppression des espaces inutiles et division en mots
    mots = line.strip().split()
    # Affichage de chaque mot avec la valeur 1
    for mot in mots:
        print(mot, "1")
