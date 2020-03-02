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
    imagepath = f'{gettempdir()}/wallpaper.jpg'
    if platform.startswith('win32'):
        from ctypes import windll
        windll.user32.SystemParametersInfoW(0x14, 0, f'{imagepath}', 0x2)
    elif platform.startswith('Darwin'):
        script = f"""tell application "Finder"
                    set desktop picture to POSIX file {imagepath}/wallpaper.jpg
                    end tell"""
        system(script)
    else:
        from os import environ
        if 'gnome' in environ.get('DESKTOP_SESSION'):
            import gconf
            conf = gconf.client_get_default()
            conf.set_string('/desktop/gnome/background/picture_filename', '/path/to/filename.jpg')
        elif 'plasma' in environ.get('DESKTOP_SESSION'):
            print("DE is kde's plasma. plasma can also natively do what this application do")
        elif 'xfce' in environ.get('DESKTOP_SESSION'):
            print('DE is xfce. currently not supported')
        else:
            print('Unknown DE')
            system(f'feh --bg-center -z -r {imagepath}')
