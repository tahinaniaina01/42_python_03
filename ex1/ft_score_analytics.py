#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/29 15:56:16 by trakotos            #+#    #+#            #
#   Updated: 2026/03/29 16:17:12 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def parse_args(args: list[str]) -> list[int]:
    l: list[int] = []
    for arg in args:
        val: int = 0
        try:
            val = int(arg)
            l += [val]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return l


def print_stat() -> None:
    scores = parse_args(sys.argv[1:])
    nb_scores = len(scores)
    if nb_scores == 0:
        print(
            "No scores provided. Usage: "
            "python3 ft_score_analytics.py <score1> <score2> ..."
        )
        return
    sum_scores = sum(scores)
    min_score = min(scores)
    max_score = max(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {nb_scores}")
    print(f"Total score: {sum_scores}")
    print(f"Average score: {sum_scores / nb_scores}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    print_stat()
    print()
