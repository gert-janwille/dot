import os
import youtube_dl
from dot.common.constants import *

def youtubeDownloader(args):
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
