from random import choice
from functions.batch_converter import makeoverlay, makebackground, combine
from ctypes import windll
from cv2 import imread, imwrite
from os.path import isdir, join, abspath
from os import walk, system

# This file contains all functions related to having the background process running

class Colortext:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    END = '\033[0m'


def settings(timer=0, folder=''):
    if timer == 0:
        print(Colortext.WARNING + 'Needs to have a timer set to bigger than 0' + Colortext.END)
        print('Set a timer in seconds to change wallpapers')
        timer = int(input('Timer:'))
    if folder == '':
        print(Colortext.WARNING + 'Needs a folder to get images from' + Colortext.END)
        folder = input('Folder path:')
    while True:
        if isdir(folder):
            break
        else:
            print(Colortext.WARNING + 'Is not a folder')
    return timer, folder


def quickwallpaper(folder, screenx, screeny):
    while True:
        files = [join(path, filename)
                 for path, dirs, files in walk(folder)
                 for filename in files]
        path = choice(files)
        image = imread(path)
        if hasattr(image, 'shape'):
            imagey, imagex, channels = image.shape
            overlay = makeoverlay(path, imagex, imagey, screenx, screeny)
            background = makebackground(path, imagex, imagey, screenx, screeny)
            wallpaper = combine(background, overlay)
            imagename = '/tmp/wallpaperfy/wallpaper.jpg'
            imwrite(imagename, wallpaper)
            break
        else:
            pass


def setwallpaper(folder, platform):
    if platform.startswith('win32'):
        path = abspath(folder)
        imagepath = path + '/' + '.wallpaper.jpg'
        windll.user32.SystemParametersInfoW(0x14, 0, imagepath, 0x2)
    elif platform.startswith('Darwin'):
        path = abspath(folder)
        imagepath = path + '/' + '.wallpaper.jpg'
        script = f"""tell application "Finder"
                    set desktop picture to POSIX file {imagepath}
                    end tell"""
        system(script)
    else:
        imagepath = '/tmp/wallpaperfy/wallpaper.jpg'
        system(f'feh --bg-center -z -r {imagepath}')
