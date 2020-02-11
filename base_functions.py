# this file contains all functions to be used by wallpaperfy base applications. that is the batch converter
import screeninfo
from cv2 import imread, GaussianBlur, BORDER_DEFAULT, INTER_AREA, imwrite, resize
from os.path import isdir, exists, join
from os import walk
from tempfile import gettempdir

def verbose(message, color='N'):
    class Colors:
        OK = '\032[94m'
        WARNING = '\032[93m'
        ERROR = '\032[91m'
        NORMAL = '\032[0m'

    if color.upper() == 'E':
        print(Colors.ERROR + message + Colors.NORMAL)
    elif color.upper() == 'W':
        print(Colors.WARNING + message + Colors.NORMAL)
    elif color.upper() == 'O':
        print(Colors.OK + message + Colors.NORMAL)
    else:
        print(message)


def get_screen_resolution(screen=''):
    if screen == '':
        screen = input("""Type the screen resolution with this format: width height. IE 1920 1080.
        or type auto to auto detect the screen resolution:""").strip()
    while True:
        if screen.upper() == 'AUTO':  # if auto detection was the chosen way to set resolution
            screen = str(screeninfo.get_monitors())
            screenx = int(screen[screen.find('width=') + 6:screen.find(',', screen.find(
                'width='))])  # screen weight
            screeny = int(screen[screen.find('height=') + 7:screen.find(',', screen.find(
                'height='))])  # screen height
            break
        elif screen[0:screen.find(' ')].isnumeric() and screen[screen.find(' ') + 1:len(
                screen)].isnumeric():  # this finds if the number in between the x that is what separates width from
            # heigth, contain only numbers
            if ' ' in screen:
                screenx = int(screen[0:screen.find(' ')])
                screeny = int(screen[screen.find(' '):len(screen)])
                break
            else:
                screen = input('Type screen resolution width height:')
        else:
            screen = input('Type screen resolution width height:')
    return screenx, screeny


def get_files(path=''):
    line = 0
    if path == '':
        path = input('Enter path to input folder:')
    while True:
        if exists(path):
            if isdir(path):
                break
            else:
                path = input('Try again:')
        else:
            path = input('Try again, another input folder:')
    wallpaperfytemp = open(f'{gettempdir()}/wallpaperfylist', 'w')
    print('Geting all file that can be converted, please wait.')
    for root, dirs, files in walk(path):
        for file in files:
            line += 1
            imagepath = join(root, file)
            image = imread(imagepath)
            print(f'{imagepath}')
            if hasattr(image, 'shape'):
                imagey, imagex, channels = image.shape
                wallpaperfytemp.write(f':LINE={line}:SIZE={imagex}x{imagey}:PATH={join(root, file)}' + '\n')
            else:
                pass  #
    wallpaperfytemp.close()


def makeoverlay(imagepath, imagex, imagey, screenx, screeny):
    scaleby = find_scale_factor(imagex, imagey, screenx, screeny)
    overlay = resize_image(imagepath, imagex, imagey, scaleby)
    return overlay


def makebackground(imagepath, imagex, imagey, screenx, screeny):
    scaleby = find_scale_factor(imagex, imagey, screenx, screeny, True)
    background = resize_image(imagepath, imagex, imagey, scaleby)
    background = GaussianBlur(background, (31, 31), BORDER_DEFAULT)
    background = crop(background, screenx, screeny)
    return background


def makewallpaper(screenx, screeny, output):
    print('Making wallpapers. Please wait')
    iteration = 0
    file = open(f'{gettempdir()}/wallpaperfylist', 'r')
    for line in file:
        iteration += 1
        imagex = line[line.find('SIZE=') + 5: line.find('x')]
        imagex = int(imagex)
        imagey = line[line.find('x') + 1: line.find(':PATH=')]
        imagey = int(imagey)
        imagepath = line[line.find(':PATH=') + 6: line.find('\n')]
        overlay = makeoverlay(imagepath, imagex, imagey, screenx, screeny)
        background = makebackground(imagepath, imagex, imagey, screenx, screeny)
        wallpaper = combine(background, overlay)
        save(f'{output}/{iteration}.jpg', wallpaper)
    print(f'Total images: {iteration}')


def find_scale_factor(imagex, imagey, screenx, screeny, background=False):
    global scaleby
    if not background:
        scaleby = screenx / imagex
        testsize = imagey * scaleby
        if testsize > screeny:
            scaleby = screeny / imagey
    else:
        scaleby = screenx / imagex
        testsize = imagey * scaleby
        if testsize < screeny:
            scaleby = screeny / imagey
    return scaleby


def resize_image(imagepath, imagex, imagey, scaleby):
    image = imread(imagepath)
    imagex = int(imagex * scaleby)
    imagey = int(imagey * scaleby)
    dim = (imagex, imagey)
    resizedimage = resize(image, dim, interpolation=INTER_AREA)
    return resizedimage


def save(name, image):  # saves new image
    imwrite(name, image)


def combine(background, overlay):
    x_offset = (background.shape[1] - overlay.shape[1]) / 2
    x_offset = int(x_offset)
    y_offset = (background.shape[0] - overlay.shape[0]) / 2
    y_offset = int(y_offset)
    wallpaper = background
    wallpaper[y_offset:y_offset + overlay.shape[0], x_offset:x_offset + overlay.shape[1]] = overlay
    return wallpaper


def crop(image, screenx, screeny):
    imagey, imagex, channels = image.shape
    cropy = (imagey - screeny) / 2
    cropx = (imagex - screenx) / 2
    if cropx < 0:
        cropx = 0
    if cropy < 0:
        cropy = 0
    cropx = int(cropx)
    cropy = int(cropy)
    crop_image = image[cropy:imagey - cropy, cropx:imagex - cropx]
    return crop_image


def get_output_folder(output=''):
    if output == '':
        output = input('Type the path to the output folder:')
    while True:
        if exists(output):
            if isdir(output):
                break
            else:
                output = input("Try again:")
        else:
            output = input('Try again:')
    return output


