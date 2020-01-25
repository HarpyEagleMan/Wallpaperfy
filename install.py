#!/bin/python
import os
import sys
import ctypes


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if sys.platform.startswith('win32'):
    if is_admin():
        pass
    # Code of your program here
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
elif sys.platform.startswith('Darwin'):
    pass
elif sys.platform.startswith('linux'):
    print('platform is linux')
    if os.path.isdir('/usr/lib/wallpaperfy'):
        print('folder already exists')
        print('Updating, removing old version and copying new one')
        os.system('sudo -S rm -rf /usr/lib/wallpaperfy')
    if os.path.isfile('/usr/bin/wallpaperfybc'):
        print('wallpaperfybc already exists, deleting it')
        os.system('sudo -S rm /usr/bin/wallpaperfybc')
    if os.path.isfile('/usr/bin/wallpaperfybp'):
        print('wallpapaerfybp already exists, deleting it')
        os.system('sudo -S rm /usr/bin/wallpaperfybp')
    os.system("sudo -S cp -r application /usr/lib/wallpaperfy")
    os.system('sudo -S cp linux/wallpaperfybc /usr/bin/wallpaperfybc')
    os.system('sudo -S cp linux/wallpaperfybp /usr/bin/wallpaperfybp')
