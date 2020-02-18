from wallpaperfy_base_functions import verbose


def settings(timer=0, folder=''):
    from os.path import isdir
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
            folder = input('Try another path')
    return timer, folder


def quickwallpaper(folder, screenx, screeny):
    from os.path import join
    from os import walk
    from random import choice
    from tempfile import gettempdir
    from cv2 import imwrite, imread
    from wallpaperfy_base_functions import makeoverlay, makebackground, combine
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
    from tempfile import gettempdir
    from os import system
    if platform.startswith('win32'):
        from ctypes import windll
        #imagepath = f'{gettempdir()}/wallpaper.jpg'  # old way of doing it
        windll.user32.SystemParametersInfoW(0x14, 0, f'{gettempdir()}/wallpaper.jpg', 0x2) # then in the middle section put imagepath
    elif platform.startswith('Darwin'):
        script = f"""tell application "Finder"
                    set desktop picture to POSIX file {gettempdir()}/wallpaper.jpg
                    end tell"""
        system(script)
    else:
        imagepath = f'{gettempdir()}/wallpaper.jpg'
        system(f'feh --bg-center -z -r {imagepath}')
