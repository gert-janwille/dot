#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import time

from dot.common.util import *
from dot.common.constants import *

import dot.modules.games.Hangman as Hangman
from dot.modules.games.DarkOutside import *

import dot.modules.scripts.Colums as Colums
from dot.modules.scripts.TorRelay import *
from dot.modules.scripts.sshConnection import *
from dot.modules.scripts.youtubeDownloader import *
import dot.modules.scripts.Messaging as Messaging

SESSION = ''

class TaskEngine:

    def __init__(self, task):
        #all commands and there functions
        options = {
            '..': self.back,
            'exit': self.stop,
            'clear': self.clear,
            'help': self.help,
            'connect': self.connect,
            'yt': self.youtubeDownload,
            'isdark': self.darkOutside,
            'hangman': self.hangman,
            'secure': self.secureNetwork,
            'flush': self.flush,
            'chat': self.secureChat
        }

        #if command exists, split the string and checks the first command
        args = task.split(' ')
        count = 0
        maxlen = len(options);

        for command, func in options.iteritems():
            if args[0] == command:
                options[command](args)
                break
            else:
                count += 1
                if count == maxlen:
                    try:
                     os.system(task)
                    except:
                        print '[' + R + '!' + W + '] Command: %s is not found.' % (task)


    def help(self, args):
        fmt = [
            (T+'Command', 'cmd', 20),
            ('Description', 'desc', 50),
            ('Options' + W, 'opt', 20)
        ]
        print(Colums.ColumGenerator(fmt, ul='=')(DATA))

    def stop(self, args):
        print '[' + R + '!' + W + '] Closing'
        print R + '\n' + O + '  • Bye! See you later :)\n' + W
        sys.exit(0)

    def clear(self, args): clearScreen(args)

    def back(self, args):
        global SESSION
        SESSION = ''

    def hangman(self, args): game = Hangman.Hangman()
    def darkOutside(self, args): darkOutside(args)

    def flush(self, args): restoreToDefault(args)
    def secureNetwork(self, args): SetupTorRelay(args)

    def youtubeDownload(self, args): youtubeDownloader(args)

    def connect(self, args): sshConnect(args)
    def secureChat(self, args): chat = Messaging.SecureMessagingChat(args)
