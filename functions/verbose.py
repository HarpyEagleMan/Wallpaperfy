# this file will contain functions to show some messages to help me debug what is happening


class colors:
    OK = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    NORMAL = '\033[0m'



def verbose(message, color='N'):
    if color.upper() == 'R':
        print(colors.FAIL + message + colors.NORMAL)
    elif color.upper() == 'Y':
        print(colors.WARNING + message + colors.NORMAL)
    elif color.upper() == 'B':
        print(colors.OK + message + colors.NORMAL)
    else:
        print(message)


verbose('hi there', 'a')