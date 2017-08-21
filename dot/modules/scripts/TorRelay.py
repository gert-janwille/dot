#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from dot.common.util import *
from dot.common.constants import *

def restoreToDefault(args):
    print '[' + T + '*' + W + '] Closing secure connection...'

    #unset proxy
    os.system('sudo networksetup -setsocksfirewallproxystate ' + INTERFACE + ' off')
    print '[' + R + '+' + W + '] Secure connection closed'

def SetupTorRelay(args):
    clearScreen(args)

    print '[' + T + '*' + W + '] Starting secure connection'

    try:
        #ask and keep on password
        os.system('sudo -v')
        os.system('while true; do sudo -n true; sleep 60; kill -0 "$$" || exit; done 2>/dev/null &')

        #relay interface through tor
        os.system('sudo networksetup -setsocksfirewallproxy ' + INTERFACE + ' 127.0.0.1 9050 off')
        os.system('sudo networksetup -setsocksfirewallproxystate ' + INTERFACE + ' on')

        print '\n[' + G + '+' + W + '] SOCKS proxy 127.0.0.1:9050 enabled'
        print '[' + G + '+' + W + '] Starting Tor engine... \n'

        #now runs tor in background
        os.system('tor &>/dev/null &')

        #countdown to secure connection
        countdown(3)
        print '[' + T + '*' + W + '] Close connection using ‘flush’'
        print '[' + G + '+' + W + '] Secure connetion established!\n You can browse anonymously.\n Want to be sure? Check: https://check.torproject.org/'

    except KeyboardInterrupt:
        print 'test interupted'
