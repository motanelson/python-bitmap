#!/usr/bin/python
from PIL import Image;
import PIL ;
import numpy as np;
def pset(images,x,y,r,g,b):
	images[y][x][0]=r;
	images[y][x][1]=g;
	images[y][x][2]=b;
n=0;
nn=0;
nnn=0;
nnnn=0;
print("\033c\033[42;30m\n");
print ("XXXX");
image1=np.zeros((64,64,3),np.uint8);
nn=range(0,63);
for n in nn:
	pset(image1,n,n,0,255,0);
for n in nn:
	pset(image1,n,63-n,0,255,0);
im=Image.fromarray(image1);
im.save("my.jpeg");
