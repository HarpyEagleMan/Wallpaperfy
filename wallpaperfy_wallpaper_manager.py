#!/bin/python
from argparse import ArgumentParser
from sys import platform
from time import sleep
from wallpaperfy_wallpaper_manager_functions.background_process import quickwallpaper, setwallpaper, settings
from communs import get_screen_resolution
from os import system

parser = ArgumentParser()

parser.add_argument('-r', '--resolution', help='The resolution of the screen that wallpapers should fit in '
                                               'use this format: width height, like this: 1920 1080, it also '
                                               'accepts "auto" as a valid value')
parser.add_argument('-t', '--timer', help='Set the time between each wallpaper change')
parser.add_argument('-i', '--input', help='Set the folder where the images to be wallpaperfied are located')
args = parser.parse_args()
if args.resolution:
    sress = args.resolution
else:
    sress = ''
if args.timer:
    stimer = args.timer
else:
    stimer = 0
if args.input:
    sfolder = args.input
else:
    sfolder = ''

try:
    system('mkdir /tmp/wallpaperfy')
except:
    pass
timer, folder = settings(stimer, sfolder)
timer = int(timer)
screenx, screeny = get_screen_resolution(sress)
screenx = int(screenx)
screeny = int(screeny)
print("""
Your wallpaper should change in a moment

If you liked this software please consider making a donation to one these crypto wallet
ethereum: 0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423
bitcoin: bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m
Monero: 45L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUXFHuND9SZju2DN8pjDbh7wEh""")
while True:
    quickwallpaper(folder, screenx, screeny)
    setwallpaper(folder, platform)
    sleep(timer)
