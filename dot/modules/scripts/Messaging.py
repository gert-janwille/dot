#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import time
from pubnub import Pubnub
import dot.common.ui as ui
from dot.common.constants import *
from dot.modules.scripts.TorRelay import *
import dot.modules.scripts.Colums as Colums

class SecureMessagingChat(object):
    def __init__(self, args):
        global pn, channel
        self.channel = 'none'
        self.pn = ''
        self.open = True

        SetupTorRelay([])

        try:
            chatroom = raw_input('[' + G + '?' + W + '] Please enter the name of chat room you want to enter: ')
            user_name = raw_input('[' + G + '?' + W + '] Please enter your name: ')

            window = ui.UiTemplate()
            window.clearScreen()

            channel = chatroom
            self.channel = chatroom

            def howmanyonline():
                pn.here_now(channel=channel, callback=_howmanyonline_callback, error=_error)

            def _howmanyonline_callback(message):
                    print "\n%s online..." % message['occupancy']

            def _error(error):
                   print(error)

            def eraseLine():
                CURSOR_UP_ONE = '\x1b[1A'
                ERASE_LINE = '\x1b[2K'
                print(CURSOR_UP_ONE + ERASE_LINE)

            def _callback(message, channel):
                   if message['user_name'] != user_name:
                       eraseLine()
                       print (T + message['user_name'] +': '+ W + message['message'])
                       print '\n%s: ' % user_name

            def _history_callback(message):
                   for msg in message[0] :
                       try:
                           if any(x in msg['message'] for x in ['left...', 'Joined...']):
                               pass
                           else:
                               print T + msg['user_name'] +": "+ W + msg['message']

                       except:
                           print ''

            def get_input():
                  message = raw_input("%s: " % user_name)
                  if str(message) in ['quit', 'QUIT', 'Quit', 'exit', 'Exit', 'EXIT']:
                      print '[' + R + '!' + W + '] Quiting secure chat...'

                      leftMsg = T + " has left... " + W
                      pn.publish(channel=channel, message=dict(user_name=user_name, message=leftMsg))

                      pn.unsubscribe(channel=channel)
                      sys.stdout.flush()
                      restoreToDefault([])
                      self.open = False
                      print '[' + G + '+' + W + '] Chat Closed!'

                  elif str(message) in ['whosonline', 'whoisonline']:
                      pn.here_now(channel=channel, callback=_whosonline_callback, error=_error)

                  elif str(message) in ['howmanyonline']:
                      howmanyonline()

                  elif str(message) in ['']:
                      pass

                  elif str(message) in ['help']:
                      fmt = [
                          (T+'Command', 'cmd', 20),
                          ('Description', 'desc', 50),
                          ('Options' + W, 'opt', 20)
                      ]
                      print(Colums.ColumGenerator(fmt, ul='=')(MSG))

                  else:
                     msg_object = dict(user_name=user_name, message=message)
                     pn.publish(channel=channel, message=msg_object)

            def _whosonline_callback(message):
                   print("Following are online :")
                   print("-------------")
                   for msg in message['uuids'] :
                       print(msg)


            pn = Pubnub(publish_key="pub-c-b3f98b74-e7d4-456f-a7a2-89346cfddc4a", subscribe_key="sub-c-8bc8b68a-8740-11e7-9034-1e9edc6dd7f6", ssl_on=False, uuid=user_name)
            self.pn = pn

            joinMsg = T + " Joined... " + W
            pn.publish(channel=channel, message=dict(user_name=user_name, message=joinMsg))

            howmanyonline()
            print '[' + T + '*' + W + '] Close chat using ‘ctrl+c’ or type ‘quit’ or ‘exit’ \n'
            print T + 'Hello %s. Welcome to %s chatroom' % (user_name, chatroom)
            print W

            pn.subscribe(channels=channel, callback=_callback)
            pn.history(channel=channel, count=10, callback=_history_callback, error=_error)
            time.sleep(1)

            while self.open:
                   get_input()

            if self.open:
                msg_object = dict(user_name=user_name, message=message)
                pn.publish(channel=channel, message=msg_object)

        except KeyboardInterrupt:
            try:
                print self.channel
                self.pn.unsubscribe(channel=self.channel)
                sys.stdout.flush()
            except:
                print 'Something went wrong'

            restoreToDefault([])
            print R + '\n' + O + '  • Quiting Chat\n' + W
