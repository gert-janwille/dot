#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import time
import curses
from dot.common.constants import *

# Fixes UnicodeDecodeError for ESSIDs
reload(sys)
sys.setdefaultencoding('utf8')

class DotEngine:

    def __init__(self):
        self.op_mode = 0x0

    def start(self):
        print('engine started')

    def stop(self):
        print "[" + G + "+" + W + "] Thanks for using!"
        print '[' + R + '!' + W + '] Closing'
        sys.exit(0)



def run():
    try:
        print ('[' + T + '*' + W + '] Starting dot %s at %s' %(VERSION, time.strftime("%Y-%m-%d %H:%M")))

        engine = DotEngine()
        engine.start()

    except KeyboardInterrupt:
        print R + '\n (^C)' + O + ' interrupted\n' + W
    except EOFError:
        print R + '\n (^D)' + O + ' interrupted\n' + W
