#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os

VERSION = "0.0.1"
INTERFACE='Wi-Fi'

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

DATA = [
    {'cmd':'..', 'desc':'goes back to mainframe', 'opt':'none'},
    {'cmd':'exit', 'desc':'exits the dot program', 'opt':'none'},
    {'cmd':'clear', 'desc':'Clears the screen', 'opt':'none'},
    {'cmd':'help', 'desc':'Lists all available options', 'opt':'none'},

    {'cmd':'\nconnect', 'desc':'connect to server using ssh,', 'opt':' -u <username>'},
    {'cmd':'', 'desc':'if no options it connects to', 'opt':'-p <password>'},
    {'cmd':'', 'desc':'default settings', 'opt':'-h <server_ip>'},

    {'cmd':'\nsecure', 'desc':'Relay all internet traffic over', 'opt':'none'},
    {'cmd':'', 'desc':'check: https://check.torproject.org/', 'opt':''},

    {'cmd':'\nflush', 'desc':'Close secure connection and set to', 'opt':'none'},
    {'cmd':'', 'desc':'default settings', 'opt':''},

    {'cmd':'\nyt', 'desc':'exits the dot program', 'opt':'-l <link>'},
    {'cmd':'isdark', 'desc':'Say in ascii if it is dark outside', 'opt':'none'},
    {'cmd':'hangman', 'desc':'Play Hangman, just type a letter', 'opt':'none\n'}
]
