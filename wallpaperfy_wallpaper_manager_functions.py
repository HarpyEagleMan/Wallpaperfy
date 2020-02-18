from os.path import isdir, join
from os import walk, system
from ctypes import windll
from random import choice
from wallpaperfy_base_functions import verbose, makebackground, makeoverlay, combine
from cv2 import imread, imwrite
from tempfile import gettempdir


def settings(timer=0, folder=''):
    if timer == 0:
        print('Set a timer in seconds to change wallpapers')
        timer = int(input('Timer:'))
    if folder == '':
        folder = input('Folder path:')
    while True:
        if isdir(folder):
            break
        else:
            verbose('Is not a folder', 'error')
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
            imagename = f'{gettempdir()}/wallpaper.jpg'
            imwrite(imagename, wallpaper)
            break
        else:
            pass
def setwallpaper(platform):
    if platform.startswith('win32'):
        imagepath = f'{gettempdir()}/wallpaper.jpg'
        windll.user32.SystemParametersInfoW(0x14, 0, imagepath, 0x2)
    elif platform.startswith('Darwin'):
        imagepath = f'{gettempdir()}/wallpaper.jpg'
        script = f"""tell application "Finder"
                    set desktop picture to POSIX file {imagepath}
                    end tell"""
        system(script)
    else:
        imagepath = f'{gettempdir()}/wallpaper.jpg'
        system(f'feh --bg-center -z -r {imagepath}')
