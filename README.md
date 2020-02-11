# Wallpaperfy

Platform agnostic wallpaper maker, and wallpaper manager.\
Turn any image into a viable wallpaper, without having to stretch, or zoom in and crop the images.\
Blank spaces that would be there due to image not perfectly filing the screen is filled with parts of the image 
that is being wallpaperfied.

I always liked how plasma desktop from kde does wallpapers, but i can't always afford to install plasma on my computers,
 or simply don't want to. Turning each image manually into an wallpaper is time consuming, so i made wallpaperfy.\
With this tool i can have wallpapers kde style but without having to install plasma desktop

Look this example:

Before Wallpaperfy
![](screenshots/Before%20Wallpaperfying.png)

After Wallpaperfy
![](screenshots/After%20Wallpaperfying.png)

# Work in progress

It's a work in progress, not every thing is working as intended.
on linux the the batch converter is working as intended
i have yet to test it on any other os. if you want to test it and give me feed back feel free to do so

# Requirements
Python 3 possible 3.8 is what i tested it.
Opencv-python a python package
screeninfo another python package
Feh if on linux and it only works on i3 and maybe other Dynamic window managers. i dont know i have not tested it yet 

# install
Copy the contents of wallpaperfy folder to where you want to install. add this place to the PATH variable or make a
simlink to Batch-converter from wherever is your PATH.

# Running
run Batch-converter for the batch converter on a terminal

# command line arguments

you can pass these as arguments for Batch-converter 
-r "1920 1080" or whattever is your scree resolution. to set the resolution of the wallpapers. or just use -r auto\
-i "path to input folder" this is where the folder containing the images to be wallpaperfied is. it will also take all
images in subfolder
-o "path to output folder" this is the folder where the images being converted will be saved to

# Donations
if you are interested in this project, please consider making a donation to this crypto wallet.


Monero
46L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUX  
FHuND9SZju2DN8pjDbh7wEh

Ethereum
0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423

Bitcoin
bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m
