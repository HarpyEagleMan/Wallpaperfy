import argparse
from sys import platform
from time import sleep

from bgprocess import *
from converter import get_screen_resolution

parser = argparse.ArgumentParser()

parser.add_argument('-r', '--screen_resolution', help='Onput the resolution of the screen that wallpapers should fit in'
                                                      'use this format: width height, like this: 1920 1080, it also '
                                                      'accepts "auto" as a valid value')
parser.add_argument('-t', '--timer', help='Set the interval between each wallpaper change')
parser.add_argument('-f', '--folder', help='Set the folder where the images to be wallpaperfied are located')
args = parser.parse_args()
print("""If you liked this software please consider making a donation to one of these crypt wallets
Bitcoin: bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m
Ethereum: 0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423
Monero: 46L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUXFHuND9SZju2DN8pjDbh7wEh""")
if args.screen_resolution:
    sress = args.screen_resolution
else:
    sress = ''
if args.timer:
    stimer = args.timer
else:
    stimer = 0
if args.folder:
    sfolder = args.folder
else:
    sfolder = ''
timer, folder = settings(stimer, sfolder)
timer = int(timer)
screenx, screeny = get_screen_resolution(sress)
screenx = int(screenx)
screeny = int(screeny)
while True:
    quickwallpaper(folder, screenx, screeny)
    setwallpaper(folder, platform)
    sleep(timer)
