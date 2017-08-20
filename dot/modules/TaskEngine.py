#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sys
import time
import shutil
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
            'hangman': self.hangman
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
                if count == maxlen: print '[' + R + '!' + W + '] Command: %s is not found.' % (task)




    def help(self, args):
        # TODO: need to show all options
        print "help"

    def stop(self, args):
        print '[' + R + '!' + W + '] Closing'
        print R + '\n' + O + '  • Bye see you later :)\n' + W
        sys.exit(0)

    def clear(self, args):
        window = ui.UiTemplate()
        window.clearScreen()

    def back(self, args):
        global SESSION
        SESSION = ''

    def hangman(self, args):
        game = Hangman.Hangman()

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
