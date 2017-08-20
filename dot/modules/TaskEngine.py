#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
from pexpect import pxssh
from dot.common.constants import *
import dot.env.credentials as credentials

SESSION = ''

class TaskEngine:

    def __init__(self, task):

        options = {
            '..': self.back,
            'exit': self.stop,
            'help': self.help,
            'connect': self.connect
        }

        args = task.split(' ')
        for command, func in options.iteritems():
            if args[0] == command:
                options[command](args)
                pass


    def help(self):
        # TODO: need to show all options
        print "help"

    def stop(self, args):
        print '[' + R + '!' + W + '] Closing'
        print R + '\n' + O + '  • Thanks for using\n' + W
        sys.exit(0)

    def back(self, args):
        global SESSION
        SESSION = ''

    def connect(self, args):

        try:
            username = args[args.index('-u') + 1]
            password = args[args.index('-p') + 1]
            hostname = args[args.index('-h') + 1]

        except:
            username = credentials.SSH_USER
            password = credentials.SSH_PASS
            hostname = credentials.KALI_SERVER

        print '[' + R + '*' + W + '] Establish ssh connection to %s ' % (hostname)

        try:
            s = pxssh.pxssh()
            s.login (hostname, username, password)
            print '[' + R + '+' + W + '] ssh connection with %s established ' % (hostname)
            print '[' + R + '+' + W + '] Your logged in as %s ' % (username)

            command = '';
            while command != 'logout':
                command = raw_input( T + 'DOT '+ W + '('+ username +'@'+ hostname +')'+ T +' > ' + W )
                if command == 'logout':
                    s.logout()
                    print '[' + R + '+' + W + '] Succesfully logged out. (%s) ' % (hostname)
                else:
                    s.sendline(command)
                    s.prompt()
                    print s.before
                pass

        except:
            print '[' + R + '!' + W + '] ssh connection to failed'
