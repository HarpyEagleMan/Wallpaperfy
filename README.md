# Wallpaperfy

Platform agnostic wallpaper maker, and wallpaper manager.\
Turn any image into a viable wallpaper, without having to stretch, or zoom in and crop the images.\
Blank spaces that would be there due to image not perfectly filing the screen is filled with parts of the image 
that is being wallpaperfied.

I always liked how plasma desktop from kde does wallpapers, but i can't always afford to install plasma on my computers,
 or simply don't want to. Turning each image manually into an wallpaper is time consuming, so made wallpaperfy.\
With this tool i can have wallpapers kde style but without having to install plasma desktop

Look this example:

Before Wallpaperfy
![](screenshots/Before%20Wallpaperfying.png)

After Wallpaperfy
![](screenshots/After%20Wallpaperfying.png)

As of this version, it only works on command line

# Requirements
# Python
Python. go to official website, https://www.python.org/ download and install it.\
Alternatively, you can use your OS package manager.\
If you are running a unix like os Python may already be installed by default.

# Opencv-python
You need to install opencv-python for this software to work. with python installed you can run this command in your 
terminal:\
pip install opencv-python\
you may need to run this with elevated privileges.

# screeninfo
This also can be installed with a terminal command if you already got python installed run this:\
pip install screeninfo\

# Feh - Only if Not on Windows or macOS
feh the image viewer is required on anything that is not Windows or macOS.\
install it from you package manager, if it is not available. you need to compile it from source.\
https://feh.finalrewind.org/

# How to use this
Download this application.\
Go click the big button that says clone or download.\
Extract the folder.\
Use 7zip or any other file extractor to get the application into a folder you wish.\
Open a terminal.\
change directory into the Application folder.\
Cd into wallpaperfy folder by typing cd "insert path to wallpaperfy folder here" without quotes.\
Run the application.\
Type: python wallpaperfybatchconverter.py in the terminal and press enter to run the batch converter and make all images
 inside a folder and its sub folders into wallpapers.\
The terminal will prompt for the folder locations and will find images within sub folders.\
alternatively, you can run wallpaperfybgprocess.py to have a background process running that will periodically change 
your wallpaper into a wallpaper created by wallpaperfy.

You can use command line arguments if you don't want to wait until the program prompt you for input.\
Just type in the command line python:\
wallpaperfybatchvconver.py -r "screen resolution" -i "path to input folder" -o "path to output folder"

you can also use arguments on the background process. Run:\
wallpaperfybgprocess.py -t "time you want for wallpaper to cicle" -i "input folders" -r "screen resolution"\
wallpaperfy-bgprocess.py will stop changing the wallpapers if the terminal running it is closed.

i can deal with whatever incovenience this application has from being a terminal applications with no installation.\
So as far as i am concerned this wallpaperfy is feature complete. but i might come back to work more on wallpaperfy if it get requests them i can make\
1 a proper installer\
2 GUI\

# Donations
if you are interested in this project, please consider making a donation to one of these crypto wallets.

Bitcoin
bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m

Ethereum
0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423

Monero
46L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUX  
FHuND9SZju2DN8pjDbh7wEh
