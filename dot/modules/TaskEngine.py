#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import time
import shutil
import webbrowser
import youtube_dl
from pexpect import pxssh
from dot.common.constants import *
import dot.common.ui as ui
import dot.env.credentials as credentials
import dot.modules.games.Hangman as Hangman

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
            'flush': self.flush
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
        # TODO: need to show all options
        print "help"

    def stop(self, args):
        print '[' + R + '!' + W + '] Closing'
        print R + '\n' + O + '  • Bye! See you later :)\n' + W
        sys.exit(0)

    def clear(self, args):
        window = ui.UiTemplate()
        window.clearScreen()

    def back(self, args):
        global SESSION
        SESSION = ''

    def hangman(self, args):
        game = Hangman.Hangman()

    def countdown(self, n) :
        while n > 0:
            print '%s...'%(n)
            time.sleep(1)
            n = n - 1
            if n ==0:
                return 0

    def flush(self, args):
        print '[' + T + '*' + W + '] Closing secure connection...'

        #unset proxy
        os.system('sudo networksetup -setsocksfirewallproxystate ' + INTERFACE + ' off')
        print '[' + R + '+' + W + '] Secure connection closed'

    def secureNetwork(self, args):
        self.clear([])

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
            self.countdown(3)
            print '[' + T + '*' + W + '] Close connection using ‘flush’'
            print '[' + G + '+' + W + '] Secure connetion established!\n You can browse anonymously.\n Want to be sure? Check: https://check.torproject.org/'

        except KeyboardInterrupt:
            print 'test interupted'

    def youtubeDownload(self, args):
        try:
            link = args[args.index('-l') + 1]
            print link
        except:
            print '[' + R + '!' + W + '] Please enter a link.'

        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            print '[' + G + '+' + W + '] File Found - Start Download'
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])

        except: print '[' + R + '!' + W + '] Download has failed, use command: \n brew install libav'

        else:
            folder = os.getcwd()
            source = os.listdir(folder)
            destination = "/Users/user/Downloads"

            for files in source:
                if files.endswith(".mp3"):
                    shutil.copy(files,destination)
                    os.remove(files)
                    print '[' + G + '+' + W + '] Completed %s' % (files)

    def connect(self, args):
        try:
            username = args[args.index('-u') + 1]
            password = args[args.index('-p') + 1]
            hostname = args[args.index('-h') + 1]

        except:
            username = credentials.SSH_USER
            password = credentials.SSH_PASS
            hostname = credentials.KALI_SERVER

        print '[' + T + '*' + W + '] Establish ssh connection to %s ' % (hostname)

        try:
            s = pxssh.pxssh()
            s.login (hostname, username, password)
            print '[' + G + '+' + W + '] ssh connection with %s established ' % (hostname)
            print '[' + G + '+' + W + '] Your logged in as %s ' % (username)
            print '[' + T + '*' + W + '] To logout use command `logout` '

            command = '';
            while command != 'logout':
                command = raw_input( T + 'DOT '+ W + '('+ username +'@'+ hostname +')'+ T +' > ' + W )
                if command == 'logout':
                    s.logout()
                    print '[' + G + '+' + W + '] Succesfully logged out. (%s) ' % (hostname)
                else:
                    s.sendline(command)
                    s.prompt()
                    print s.before
                pass

        except:
            print '[' + R + '!' + W + '] ssh connection to failed'


    def darkOutside(self, args):
        print("Is it dark outside?\n==================")

        #get the structure containing the current time
        time_now = time.localtime()
        if time_now.tm_hour >=DARK_HOUR[time_now.tm_mon] or time_now.tm_hour < LIGHT_HOUR[time_now.tm_mon]:
            print(' /$$     /$$ /$$$$$$$$  /$$$$$$ ')
            print('|  $$   /$$/| $$_____/ /$$__  $$')
            print(' \  $$ /$$/ | $$      | $$  \__/')
            print('  \  $$$$/  | $$$$$   |  $$$$$$ ')
            print('   \  $$/   | $$__/    \____  $$')
            print('    | $$    | $$       /$$  \ $$')
            print('    | $$    | $$$$$$$$|  $$$$$$/')
            print('    |__/    |________/ \______/ ')

        else:
            print(' /$$   /$$  /$$$$$$ ')
            print('| $$$ | $$ /$$__  $$')
            print('| $$$$| $$| $$  \ $$')
            print('| $$ $$ $$| $$  | $$')
            print('| $$  $$$$| $$  | $$')
            print('| $$\  $$$| $$  | $$')
            print('| $$ \  $$|  $$$$$$/')
            print('|__/  \__/ \______/ ')
