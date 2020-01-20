# Wallpaperfy

<strike>Platform agnostic wallpaper maker</strike>, right now it only  
works on Windows 10, and only on command line.\
Turn any image into a viable
wallpaper. without having to stretch, or zoom in and crop the images.  
blank spaces that would be there due to image not perfectly filing the  
screen is filled with parts of the image that is being wallpaperfied

I always liked how plasma desktop from kde does wallpapers, but i can't  
always afford to install plasma on my computers, or simply don't want  
 to.\
But turning each image manualy into an wallpaper is time consuming,  
so i am making this alternative. This way i can have wallpaper kde style  
 but without having to install plasma desktop

Of course i will share with everybody with this opensource license.

this is an example of image before using wallpaperfy
![](screenshots/Before%20Wallpaperfying.png)

and this is after
![](screenshots/After%20Wallpaperfying.png)

It already works if you dont mind working on the command line.

# Requirements
# Python
Python. go to official website, https://www.python.org/ download and  
install it. alternatively. you can use your OS package manager.\
If you are on unix like os this may already be installed by default.

# Opencv-python
You need to install opencv-python for this software to work. with python  
 installed you can run this command in your terminal:\
pip install opencv-python\
you may need to run this with elevated privileges.

# screeninfo
This also can be installed with a terminal command if you already got  
python installed run this:\
pip install screeninfo.

# How to use this
# 1 Download this application
Go click the big button that says clone or download.

# 2 Extract the folder
Use 7zip or any other file extractor to get the application into a  
folder you wish.

# 3 Open a terminal
Be it powershell, cmd, xterm. Whatever is the terminal on you OS.

# 4 Cd into the Application root folder
Cd into wallpaperfy root folder by typing cd "insert path to wallpaperfy  
 folder here" without quotes.

# 5 Run the application
Type: python wallpaperfy-batchconverter.py in the terminal and press  
enter to run the batch converter and make all images inside a folder and  
 its subfolders into wallpapers.\
The terminal will prompt for the folder locations and will find images  
within subfolders.\
alternatively, you can run wallpaperfy-bgprocess.py to have a backgroud  
process running that will periodicaly change your wallpaper into a  
wallpaper created by wallpaperfy.

you can use command line arguments if you dont want to wait untill the  
program prompt you for input just type in the command line python  
wallpaperfy-batchvconver.py -r "screen resolution" -i "path to input  
folder" -o "path to output folder"

you can also use arguments on the background process. run  
wallpaperfy-bgprocess.py -t "time you want for wallpaper to cicle" -i  
"input folders" -r "screen resolution" wallpaperfy-bgprocess.py terminal  
 will stop changing the wallpapers if the terminal running it is closed.

# Donations
if you are interested in this project, please consider making a donation  
 to one of these crypto wallets.

Bitcoin
bc1qfctjg78yspl66m65kchjaceuhtqsnekscn9v7m

Ethereum
0xa69aE6A70F15fb3ACBccFbd9B962582d44A98423

Monero
46L5E2tFT7K4G1GZwAuLyGQx82KeQeaCyLNZ9TtPzDWdcchV1x4Xwc2VgzPLUXS4gQ8fYLUX  
FHuND9SZju2DN8pjDbh7wEh
