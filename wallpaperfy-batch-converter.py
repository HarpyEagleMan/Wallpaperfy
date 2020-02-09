#!/bin/python
from argparse import ArgumentParser
from functions.batch_converter import get_screen_resolution, get_files, get_output_folder, makewallpaper
from os import system

parser = ArgumentParser()
parser.add_argument('-r', '--screen_resolution', help='Onput the resolution of the screen that wallpapers should fit in'
                                                      'use this format: width height, like this: 1920 1080, it also '
                                                      'accepts "auto" as a valid value')
parser.add_argument('-i', '--input', help='Folder from where the images will be taken to make wallpapers')
parser.add_argument('-o', '--output', help='Folder to where the wallpaper will be saved')
args = parser.parse_args()

if args.screen_resolution:
    screenress = args.screen_resolution
else:
    screenress = ''
if args.input:
    inputfolder = args.input
else:
    inputfolder = input('Type the path to input folder:')
if args.output:
    outputfolder = args.output
else:
    outputfolder = input('Type the path to output folder:')
try:
    system('mkdir /tmp/wallpaperfy')
except:
    pass
screenx, screeny = get_screen_resolution(screenress)
screenx = int(screenx)
screeny = int(screeny)
get_files(inputfolder)
outputfolder = get_output_folder(outputfolder)
makewallpaper(screenx, screeny, outputfolder)
print('Job is done!')
print("""If you liked this software please consider making a donation to this crypto wallets
Monero: 46L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUXFHuND9SZju2DN8pjDbh7wEh""")
