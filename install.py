#!python # todo add a way to change shebang accodring to what os is running it because this one does not work on linux
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
        os.makedirs('C:/Program Files/wallpaperfy')
        shutil.copy2('bgprocess.py', 'C:/Program Files/wallpaperfy')
        shutil.copy2('converter.py', 'C:/Program Files/wallpaperfy')
        shutil.copy2('wallpaperfybc.py', 'C:/Program Files/wallpaperfy')
        shutil.copy2('wallpaperfybp.py', 'C:/Program Files/wallpaperfy')
    else:
        print('you need to run this as admininstrator')
elif sys.platform.startswith('Darwin'):
    pass
elif sys.platform.startswith('linux'):
    print('platform is linux')
    if os.path.isdir('/usr/lib/wallpaperfy'):
        print('folder already exists')
        print('Updating, removing old version and copying new one')
        os.system('sudo rm -rf /usr/lib/wallpaperfy/')
    if os.path.islink('/bin/wallpaerfybc'):
        print('symbol link already exist for wallpaperfybc')
        os.system('sudo rm /bin/wallpaperfybc')
    if os.path.islink('/bin/wallpaperfybp'):
        print('symbolik link already exist for wallpaperfybp')
        os.system('sudo rm /bin/wallpaperfybp')
    os.makedirs("/usr/lib/wallpaperfy")
    shutil.copy2('wallpaperfybc.py', '/usr/lib/wallpaperfy')
    shutil.copy2('wallpaperfybp.py', '/usr/lib/wallpaperfy')
    shutil.copy2('bgprocess.py', '/usr/lib/wallpaperfy')
    shutil.copy2('converter.py', '/usr/lib/wallpaperfy')
    os.system('sudo ln -s /usr/lib/wallpaperfy/wallpaperfybc.py /bin/wallpaperfybc')
    os.system('sudo ln -s /usr/lib/wallpaperfy/wallpaperfybp.py /bin/wallpaperfybp')
    os.system('sudo chmod +x /usr/lib/wallpaperfy/wallpaperfybc.py')
    os.system('sudo chmod +x /usr/lib/wallpaperfy/wallpaperfybp.py')
