from argparse import ArgumentParser
from wallpapaerfy_base_functions import get_screen_resolution, get_files, get_output_folder, makewallpaper


# Argument handling
parser = ArgumentParser()
parser.add_argument('-r', '--resolution', help='The resolution of the screen that wallpapers should fit in'
                                               'use this format: width height, like this: 1920 1080, it also '
                                               'accepts "auto" as a valid value')
parser.add_argument('-i', '--input', help='Folder from where the images will be taken to make wallpapers')
parser.add_argument('-o', '--output', help='Folder to where the wallpaper will be saved')
args = parser.parse_args()

# parsing arguments
if args.resolution:
    screenress = args.resolution
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

# end argument handling
# Batch converting
screenx, screeny = get_screen_resolution(screenress)
screenx = int(screenx)
screeny = int(screeny)
get_files(inputfolder)
outputfolder = get_output_folder(outputfolder)
makewallpaper(screenx, screeny, outputfolder)
print('Job is done!')
print("""If you liked this software please consider making a donation to this crypto wallets
ethereum: 0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423
bitcoin: bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m
Monero: 45L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUXFHuND9SZju2DN8pjDbh7wEh""")
