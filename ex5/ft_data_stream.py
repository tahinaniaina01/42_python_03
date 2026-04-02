#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/02 11:20:36 by trakotos            #+#    #+#            #
#   Updated: 2026/04/02 16:28:32 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import typing
import random


def gen_event(
    names: list[str], actions: list[str]
) -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(names), random.choice(actions))


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    nb_events = len(events) - 1
    while events:
        i = random.randint(0, nb_events)
        nb_events -= 1
        yield events.pop(i)


def get_event_list() -> list[tuple[str, str]]:
    player_names = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "swim", "release"]
    g = gen_event(player_names, actions)
    res: list[tuple[str, str]] = []
    for i in range(1000):
        ev = next(g)
        name, action = ev
        res += [ev]
        print(f"Event {i}: Player {name} did action {action}")
    return res


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    events = get_event_list()
    ten_events = [random.choice(events) for _ in range(10)]
    consume_events = consume_event(ten_events)
    print(f"Built list of 10 events: {ten_events}")
    for _ in range(10):
        try:
            print(f"Got event from list: {next(consume_events)}")
            print(f"Remains in list: {ten_events}")
        except StopIteration:
            print("list is empty")
