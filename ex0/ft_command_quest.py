#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/29 15:43:40 by trakotos            #+#    #+#            #
#   Updated: 2026/03/29 15:54:41 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys

if __name__ == "__main__":
    args = sys.argv
    len_args = len(args)
    print("=== Command Quest ===")
    print(f"Program name:  {args[0]}")
    if len_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len_args - 1}")
        for i in range(len_args - 1):
            print(f"Argument {i + 1}: {args[i + 1]}")
    print(f"Total arguments: {len_args}\n")
