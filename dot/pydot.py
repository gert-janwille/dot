#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import time
import dot.common.ui as ui
import dot.modules.TaskEngine as TaskEngine
from dot.common.constants import *
from dot.common.arguments import *

# Fixes UnicodeDecodeError for ESSIDs
reload(sys)
sys.setdefaultencoding('utf8')

args = 0
task = ''

def check_args(args):
    if args.task :
        pid = TaskEngine.TaskEngine(args.task)


class DotEngine:

    def __init__(self):
        self.op_mode = 0x0

    def start(self):
        print '[' + R + '+' + W + '] Engine Started'

        # Parse args
        global args, task
        args = parse_args()

        # Check args
        check_args(args)

        #starts the dot input session
        while True:
            task = raw_input( T + 'DOT '+ TaskEngine.SESSION +'> ' + W )
            pid = TaskEngine.TaskEngine(task)
            pass


def run():
    try:
        window = ui.UiTemplate()
        window.clearScreen()

        print ('[' + T + '*' + W + '] Starting dot %s at %s' %(VERSION, time.strftime("%Y-%m-%d %H:%M")))

        #starts the dot engine
        engine = DotEngine()
        engine.start()

    except KeyboardInterrupt:
        print R + '\n' + O + '  • interrupted by user\n' + W
    except EOFError:
        print R + '\n' + O + '  • interrupted by error\n' + W
