#!/usr/bin/env python3

import sys

current_word = None
current_count = 0


for line in sys.stdin:
    # Découpe la ligne en mots et en valeurs
    word, count = line.strip().split()
    count = int(count)

    # Si on passe à un nouveau mot, on affiche l'ancien mot et son total
    if current_word == word:
        current_count += count
    else:
        if current_word is not None:
            print(current_word, " ", current_count)
        current_word = word
        current_count = count

# Afficher le dernier mot s'il y en a un
if current_word is not None:
    print(current_word, " ", current_count)
