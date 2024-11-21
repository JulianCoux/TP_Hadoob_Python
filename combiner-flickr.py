#!/usr/bin/env python3

import sys

current_code = None
current_count = 0

dict_count_code = {}

for line in sys.stdin:
    # Découpe la ligne en mots et en valeurs
    code, count = line.strip().split()
    count = int(count)

    # Si on passe à un nouveau mot, on affiche l'ancien mot et son total
    if current_code == code:
        current_count += count
    else:
        if current_code is not None:
            dict_count_code[current_code] = current_count
            print(current_code, " ", current_count)
        current_code = code
        current_count = count

# Afficher le dernier mot s'il y en a un
if current_code is not None:
    dict_count_code[current_code] = current_count
    print(current_code, " ", current_count)

