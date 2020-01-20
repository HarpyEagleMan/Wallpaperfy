import argparse

import converter

parser = argparse.ArgumentParser()
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
    inputfolder = ''
if args.output:
    outputfolder = args.output
else:
    outputfolder = ''

screenx, screeny = converter.get_screen_resolution(screenress)
screenx = int(screenx)
screeny = int(screeny)
converter.get_files(inputfolder)
output = converter.get_output_folder(outputfolder)
converter.makewallpaper(screenx, screeny, output)
print('Job is done!')
