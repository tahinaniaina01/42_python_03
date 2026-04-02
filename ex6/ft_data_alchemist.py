#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/02 16:32:56 by trakotos            #+#    #+#            #
#   Updated: 2026/04/02 16:55:36 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    names = [
        "Alice",
        "bob",
        "Charlie",
        "dylan",
        "Emma",
        "Gregory",
        "john",
        "kevin",
        "Liam",
    ]
    print(f"Initial list of players: {names}")
    try:
        nc = [n.capitalize() for n in names]
        names_only_capitalized = [n for n in names if n == n.capitalize()]
        print(f"New list with all names capitalized: {nc}")
        print(f"New list of capitalized names only: {names_only_capitalized}")
        print()
    except Exception as e:
        print(f"Error: {e}")
    scores = {k: random.randint(0, 1000) for k in nc}
    average = round(sum(scores.values()) / len(scores), 1)
    print(f"Score dict: {scores}")
    print(f"Score average is {average}")
    high_score = {k: scores[k] for k in nc if scores[k] >= average}
    print(f"High scores: {high_score}")
