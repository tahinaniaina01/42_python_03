#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/01 17:16:27 by trakotos            #+#    #+#            #
#   Updated: 2026/04/02 11:15:37 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def split(s: str, delim: str) -> list[str]:
    if len(delim) != 1:
        raise TypeError(f"parameters '{delim}' is not a chr")
    res: list[str] = []
    tmp: str = ""
    for c in s:
        if c == delim and tmp != "":
            res += [tmp]
            tmp = ""
        if c != delim:
            tmp += c
    res += [tmp]
    return res


def update_dict(dict: dict[str, int], key: str, val: str) -> None:
    try:
        v = int(val)
        dict.update({key: v})
    except ValueError as e:
        print(f"Quantity error for '{key}': {e}")
    except TypeError as e:
        print(e)


def parse(args: list[str]) -> dict[str, int]:
    res: dict[str, int] = {}
    for arg in args:
        try:
            val = split(arg, ":")
            if len(val) != 2:
                raise ValueError(f"Error - invalid parameter '{arg}'")
            key, value = val
            if key in res.keys():
                raise Exception(f"Redundant item '{key}' - discarding")
            update_dict(res, key, value)
        except Exception as e:
            print(e)
    return res


def display_info(inventory: dict[str, int]) -> None:
    key_lists = list(res.keys())
    max_value: tuple[str, int] = ("key", -2147483648)
    min_value: tuple[str, int] = ("key", 2147483647)
    print(f"Got inventory: {res}")
    print(f"Item list: {key_lists}")
    print(
        f"Total quantity of the {len(key_lists)} " f"items: {sum(inventory.values())}"
    )
    if len(inventory) == 0:
        return
    for key in inventory.keys():
        if max_value[1] < inventory[key]:
            max_value = (key, inventory[key])
        if min_value[1] > inventory[key]:
            min_value = (key, inventory[key])
        q = round(inventory[key] * 100 / 12, 1)
        print(f"Item {key} represents {q}%")
    print(f"Item most abundant: {max_value[0]} with quantity {max_value[1]}")
    print(f"Item least abundant: {min_value[0]} with quantity {min_value[1]}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    res = parse(sys.argv[1:])
    display_info(res)
    update_dict(res, "magic_item", "1")
    print(f"Updated inventory: {res}")
