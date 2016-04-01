### Driver Drowsiness Detection

This is course project for Gullimero Sappiro's Image/ Video Processing class - ECE590.01. 

######Build Instruction
* Assuming you have `Python 2.7` installed on your system, clone git repo using:

        git clone https://github.com/TomWoo/drowsiness-detection.git

* Assuming you have `pip` installed on your system, installed dependencies using:

        sudo pip install numpy && sudo pip install matplotlib

  If you donot have `pip` installed on your system, you can use `sudo easy_install pip` or download `get-pip.py` python script and run it. If you already have pip installed, you might want to update it using `sudo pip install -U pip`. Note that you might want to add you <path>/Python27/ and <path>/Python27/scripts to your PATH environment variable if you are using windows. 
  
* To run this project, you need verion 3.1 for OpenCV. Older verions can work but I haven't tried them. Since I am using 32 bit version of Python, I downloaded the OpenCV 3.1 binaries.

* After extracting the folder, go to `opencv/build/python/2.7` and copy `cv2.pyd` to your `'Python27/Lib/site-packages` folder. 

* This should get OpenCV running and to test it, try - `import cv2` - inside python interpreter. 

* Finally, for Windows add the dll files `opencv_ffmpeg310.dll` and `opencv_ffmpeg310_64.dll` to your Python27 folder. You can find these files inside the bin folder of your downloaded opencv binaries. 
