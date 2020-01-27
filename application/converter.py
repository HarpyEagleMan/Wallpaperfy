import screeninfo
import cv2
import os


# this file contains all functions related to converting images to wallpaper
class Colortext:
    SUCCESS = '\033[92m'
    WARNING = '\033[93m'
    END = '\033[0m'


def verbose(message):
    global verboseon
    if verboseon:
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
                print(
                    Colortext.WARNING + '\033[92m'"bad resolution, type only numbers with a space in between then"
                                        ", like this 1920 1080." + Colortext.END)
                screen = input('Type screen resolution width height:')
        else:
            print(
                Colortext.WARNING + '\033[92m'"bad resolution, type only numbers with a space in between then,"
                                    " like this 1920 1080." + Colortext.END)
            screen = input('Type screen resolution width height:')
    print(f'resolution set to {screenx}x{screeny}')
    return screenx, screeny


def get_files(path=''):
    line = 0
    if path == '':
        path = input('Enter path to input folder:')
    while True:
        if os.path.exists(path):
            if os.path.isdir(path):
                break
            else:
                print(Colortext.WARNING + 'Its not a folder' + Colortext.END)
                path = input('Try again:')
        else:
            print(Colortext.WARNING + 'It does not exist' + Colortext.END)
            path = input('Try again:')
    wallpaperfytemp = open('.wallpaperfytemp', 'w')
    print('Geting all file that can be converted, please wait.')
    for root, dirs, files in os.walk(path):
        for file in files:
            line += 1
            imagepath = os.path.join(root, file)
            image = cv2.imread(imagepath)
            print(f'{imagepath}')
            if hasattr(image, 'shape'):
                imagey, imagex, channels = image.shape
                wallpaperfytemp.write(f':LINE={line}:SIZE={imagex}x{imagey}:PATH={os.path.join(root, file)}' + '\n')
                print(Colortext.SUCCESS + 'Can be converted' + Colortext.END)
            else:
                print(Colortext.WARNING + "Can't convert" + Colortext.END)
    wallpaperfytemp.close()


def makeoverlay(imagepath, imagex, imagey, screenx, screeny):
    scaleby = find_scale_factor(imagex, imagey, screenx, screeny)
    overlay = resize(imagepath, imagex, imagey, scaleby)
    return overlay


def makebackground(imagepath, imagex, imagey, screenx, screeny):
    scaleby = find_scale_factor(imagex, imagey, screenx, screeny, True)
    background = resize(imagepath, imagex, imagey, scaleby)
    background = cv2.GaussianBlur(background, (31, 31), cv2.BORDER_DEFAULT)
    background = crop(background, screenx, screeny)
    return background


def makewallpaper(screenx, screeny, output):
    print('Making wallpapers. Please wait')
    iteration = 0
    file = open('.wallpaperfytemp', 'r')
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


def resize(imagepath, imagex, imagey, scaleby):
    image = cv2.imread(imagepath)
    imagex = int(imagex * scaleby)
    imagey = int(imagey * scaleby)
    dim = (imagex, imagey)
    resizedimage = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return resizedimage


def save(name, image):  # saves new image
    cv2.imwrite(name, image)


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
        if os.path.exists(output):
            if os.path.isdir(output):
                break
            else:
                print(Colortext.WARNING + 'this is not a folder')
                output = input("Try again:")
        else:
            print(Colortext.WARNING + 'This path does not exist')
            output = input('Try again:')
    return output

# todo there is problem are running this on linux without root privileges. need to fix where the wallpapaertemp file
#  containing all the list of wallpaper is stored. as well as where the bgprocess stores its file