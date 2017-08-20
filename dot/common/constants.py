#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

VERSION = "0.0.1"

# Console colors
W = '\033[0m'    # white (normal)
R = '\033[31m'   # red
G = '\033[32m'   # green
O = '\033[33m'   # orange
B = '\033[34m'   # blue
P = '\033[35m'   # purple
C = '\033[36m'   # cyan
GR = '\033[37m'  # gray
T = '\033[93m'   # tan

WORDS = ["pizza", "hangman", "chairs", "backpack", "bodywash", "clothing",
         "computer", "python", "program", "glasses", "sweatshirt",
         "sweatpants", "mattress", "friends", "clocks", "biology",
         "algebra", "suitcase", "knives", "ninjas", "shampoo", "php", "html", "css",
         "metasploit", "belgian waffle"
         ]

#month_number : sunset_hour
DARK_HOUR = {
    1: 16,
    2: 17,
    3: 18,
    4: 19,
    5: 19,
    6: 20,
    7: 20,
    8: 19,
    9: 18,
    10: 17,
    11: 16,
    12: 16
}

#month_number : sunrise_hour
LIGHT_HOUR = {
    1: 8,
    2: 7,
    3: 6,
    4: 5,
    5: 4,
    6: 4,
    7: 4,
    8: 5,
    9: 6,
    10: 6,
    11: 7,
    12: 8
}
