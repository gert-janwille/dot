#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import os
import sys
import time
from pubnub import Pubnub
import dot.common.ui as ui
from dot.common.constants import *
from dot.modules.scripts.TorRelay import *

'''
TODO:
    - import tor relay and start tor. When close chat flush all

'''
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

            def _callback(message, channel):
                   if message['user_name'] != user_name:
                       print T + message['user_name'] +': '+ W + message['message']
                       print "%s: hsdd " % user_name

            def _history_callback(message):
                   for msg in message[0] :
                       print T + msg['user_name'] +": "+ W + msg['message']

            def get_input():
                  message = raw_input("%s: " % user_name)
                  if str(message) in ['quit', 'QUIT', 'Quit', 'exit', 'Exit', 'EXIT']:
                      print '[' + R + '!' + W + '] Quiting secure chat...'
                      pn.unsubscribe(channel=channel)
                      sys.stdout.flush()
                      restoreToDefault([])
                      self.open = False
                      print '[' + G + '+' + W + '] Chat Closed!'

                  elif str(message) in ['whosonline', 'whoisonline']:
                      pn.here_now(channel=channel, callback=_whosonline_callback, error=_error)

                  elif str(message) in ['howmanyonline']:
                      howmanyonline()

                  else:
                     msg_object = dict(user_name=user_name, message=message)
                     pn.publish(channel=channel, message=msg_object)

            def _whosonline_callback(message):
                   print("Following are online :")
                   print("-------------")
                   for msg in message['uuids'] :
                       print(msg)


            pn = Pubnub(publish_key="pub-c-93b40064-d7f2-4ef3-a263-cfe54099495d", subscribe_key="sub-c-fb97fd92-8720-11e7-bdc2-6e5eeb112503", ssl_on=False, uuid=user_name)
            self.pn = pn

            howmanyonline()
            print T + 'Hello %s. Welcome to %s chatroom' % (user_name, chatroom)
            print W

            pn.subscribe(channels=channel, callback=_callback)
            pn.history(channel=channel, count=100, callback=_history_callback, error=_error)
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
