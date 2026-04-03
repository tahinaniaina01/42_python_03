#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/30 17:58:57 by trakotos            #+#    #+#            #
#   Updated: 2026/04/03 17:22:48 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random

achievements_list = [
    "Crafting Genius",
    "Strategist",
    "World Savior",
    "Speed Runner",
    "Survivor",
    "Master Explorer",
    "Treasure Hunter",
    "Unstoppable",
    "First Steps",
    "Collector Supreme",
    "Untouchable",
    "Sharp Mind",
    "Boss Slayer",
]


class Player:
    def __init__(self, name: str):
        self.name = name
        self.achievements = gen_player_achievements()


def gen_player_achievements() -> set[str]:
    tmp = achievements_list[:]
    res: set[str] = set()
    if len(tmp) == 0:
        return res
    nb_achievements = random.randint(1, len(tmp))
    for i in range(nb_achievements):
        random.shuffle(tmp)
        res.add(tmp.pop(0))
    return res


def difference(pa: set[str], achivements: list[set[str]]) -> set[str]:
    res = pa
    for a in achivements:
        res = res.difference(a)
    return res


if __name__ == "__main__":
    players_name = ["Alice", "Bob", "Charlie", "Dylan"]
    players = [Player(name) for name in players_name]
    u: set[str] = set()
    inter: set[str] | None = None
    only_has: list[tuple[str, set[str]]] = []
    for player in players:
        u = u.union(player.achievements)
        inter = (
            player.achievements
            if inter is None
            else inter.intersection(player.achievements)
        )
        a = [p.achievements for p in players if p.name != player.name]
        only_has += [(player.name, difference(player.achievements, a))]

        print(f"Player {player.name}: {player.achievements}")

    missings = [(p.name, u.difference(p.achievements)) for p in players]
    print()
    print(f"All distinct achievements: {u}\n")
    print(f"Common achievements: {inter}\n")
    for name, achievements in only_has:
        print(f"Only {name} has: {achievements}")
    print()
    for name, m in missings:
        print(f"{name} is missing: {m}")
