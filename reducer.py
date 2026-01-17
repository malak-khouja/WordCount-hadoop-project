#!/usr/bin/env python3
import sys

current_word = None
current_count = 0

# Lecture de l'entrée triée par Hadoop
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Affichage du mot et du total
            print(current_word + "\t" + str(current_count))
        current_word = word
        current_count = count

# Dernier mot
if current_word == word:
    print(current_word + "\t" + str(current_count))

