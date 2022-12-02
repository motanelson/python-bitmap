#!/usr/bin/python
from PIL import Image;
import PIL ;
import numpy as np;
#import cv2;
n=0;
nn=0;
nnn=0;
nnnn=0;
print("\033c\033[42;30m\n");
print ("XXXX");
image1=np.zeros((64,64,3),np.uint8);
nn=range(0,63);
for n in nn:
	image1[n][n][1]=255;
for n in nn:
	image1[n][63-n][1]=255;
im=Image.fromarray(image1);
im.save("my.jpeg");
