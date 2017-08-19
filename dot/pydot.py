#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import time
import curses
import argparse
from dot.common.constants import *
import dot.common.ui as ui

# Fixes UnicodeDecodeError for ESSIDs
reload(sys)
sys.setdefaultencoding('utf8')

args = 0

def parse_args():
    # Create the arguments
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-jI",
        "--jamminginterface",
        help=("Manually choose an interface that supports monitor mode for " +
              "deauthenticating the victims. " +
              "Example: -jI wlan1"
              )
    )

    return parser.parse_args()

class DotEngine:

    def __init__(self):
        self.op_mode = 0x0

    def stop(self):
        print "[" + G + "+" + W + "] Thanks for using!"
        print '[' + R + '!' + W + '] Closing'
        sys.exit(0)

    def start(self):
        print('engine started')

        # Parse args
        global args
        args = parse_args()

        print args




def run():
    try:
        window = ui.UiTemplate()
        window.clearScreen()
        
        print ('[' + T + '*' + W + '] Starting dot %s at %s' %(VERSION, time.strftime("%Y-%m-%d %H:%M")))

        engine = DotEngine()
        engine.start()

    except KeyboardInterrupt:
        print R + '\n (^C)' + O + ' interrupted\n' + W
    except EOFError:
        print R + '\n (^D)' + O + ' interrupted\n' + W
