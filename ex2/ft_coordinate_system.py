#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/29 16:19:27 by trakotos            #+#    #+#            #
#   Updated: 2026/04/03 17:13:12 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import math


class InputError(Exception):
    pass


def get_player_pos() -> tuple[float, float, float]:
    coords: list[float] = []
    datas = input(
        "Enter new coordinates as floats in format 'x,y,z': "
    ).split(",")
    if len(datas) != 3:
        raise InputError("Invalid syntax")
    for data in datas:
        val: float = 0.0
        try:
            val = float(data)
        except ValueError as e:
            raise ValueError(f"Error on parameter '{data}': {e}")
        except Exception as e:
            raise e
        coords += [val]
    return (coords[0], coords[1], coords[2])


def test_get_player_pos() -> tuple[float, float, float]:
    coord: tuple[float, float, float] | None = None
    while coord is None:
        try:
            coord = get_player_pos()
        except Exception as e:
            print(e)
    return coord


def calcul_distance(
    v1: tuple[float, float, float], v2: tuple[float, float, float]
) -> float:
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    center = (0.0, 0.0, 0.0)
    coord1 = test_get_player_pos()
    distance = round(calcul_distance(center, coord1), 4)
    x1, y1, z1 = coord1
    print(f"Got a first tuple: {coord1}")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {distance}")
    print()
    print("Get a second set of coordinates")
    coord2 = test_get_player_pos()
    distance = round(calcul_distance(coord1, coord2), 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")
