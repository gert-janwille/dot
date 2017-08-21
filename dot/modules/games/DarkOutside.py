import time
from dot.common.constants import *

def darkOutside(args):
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
