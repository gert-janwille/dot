from pexpect import pxssh
from dot.common.constants import *
import dot.settings as credentials

def sshConnect(args):
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
