from ctypes import windll
from os import system, makedirs
from os.path import isdir, islink
from shutil import rmtree, copy2
from sys import platform


def is_admin():
    try:
        return windll.shell32.IsUserAnAdmin()
    except:
        return False


if platform.startswith('win32'):
    print('Platform is windows')
    if is_admin():
        if isdir("C:/Program Files/wallpaperfy"):
            print('old installation detected, removing it and reinstalling')
            rmtree('C:/Program Files/wallpaperfy')
        makedirs('C:/Program Files/wallpaperfy')
        copy2('functions/background_process.py', 'C:/Program Files/wallpaperfy')
        copy2('functions/batch_converter.py', 'C:/Program Files/wallpaperfy')
        copy2('wallpaperfybc.py', 'C:/Program Files/wallpaperfy')
        copy2('wallpaperfybp.py', 'C:/Program Files/wallpaperfy')
    else:
        print('you need to run this as admininstrator')
elif platform.startswith('Darwin'):
    pass
elif platform.startswith('linux'):
    print('platform is linux')
    if isdir('/usr/lib/wallpaperfy'):
        print('folder already exists')
        print('Updating, removing old version and copying new one')
        system('sudo rm -rf /usr/lib/wallpaperfy/')
    if islink('/bin/wallpaerfybc'):
        print('symbol link already exist for wallpaperfybc')
        system('sudo rm /bin/wallpaperfybc')
    if islink('/bin/wallpaperfybp'):
        print('symbolik link already exist for wallpaperfybp')
        system('sudo rm /bin/wallpaperfybp')
    makedirs("/usr/lib/wallpaperfy")
    copy2('wallpaperfybc.py', '/usr/lib/wallpaperfy')
    copy2('wallpaperfybp.py', '/usr/lib/wallpaperfy')
    copy2('functions/background_process.py', '/usr/lib/wallpaperfy')
    copy2('functions/batch_converter.py', '/usr/lib/wallpaperfy')
    system('sudo ln -s /usr/lib/wallpaperfy/wallpaperfybc.py /bin/wallpaperfybc')
    system('sudo ln -s /usr/lib/wallpaperfy/wallpaperfybp.py /bin/wallpaperfybp')
    system('sudo chmod +x /usr/lib/wallpaperfy/wallpaperfybc.py')
    system('sudo chmod +x /usr/lib/wallpaperfy/wallpaperfybp.py')
