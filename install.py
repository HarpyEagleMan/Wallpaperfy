#!python
import os
import sys
import ctypes
import shutil


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if sys.platform.startswith('win32'):
    print('Platform is windows')
    if is_admin():
        if os.path.isdir("C:/Program Files/wallpaperfy"):
            print('old installation detected, removing it and reinstalling')
            shutil.rmtree('C:/Program Files/wallpaperfy')
        shutil.copytree('application', 'C:/Program Files/wallpaperfy')
    else:
        print('you need to run this as admininstrator')
elif sys.platform.startswith('Darwin'):
    pass
elif sys.platform.startswith('linux'):
    print('platform is linux')
    if os.path.isdir('/usr/lib/wallpaperfy'):
        print('folder already exists')
        print('Updating, removing old version and copying new one')
        shutil.rmtree('/usr/lib/wallpaperfy')
    if os.path.isfile('/usr/bin/wallpaperfybc'):
        print('wallpaperfybc already exists, deleting it')
        os.remove('/usr/bin/wallpaperfybc')
    if os.path.isfile('/usr/bin/wallpaperfybp'):
        print('wallpapaerfybp already exists, deleting it')
        os.remove('/usr/bin/wallpaperfybp')
    shutil.copytree("application", "/usr/lib/wallpaperfy")
    shutil.copyfile('linux/wallpaperfybc', '/usr/bin/wallpaperfybc')
    shutil.copyfile('linux/wallpaperfybp', '/usr/bin/wallpaperfybp')
