#!/usr/bin/python
from PIL import Image;
import PIL ;
import numpy as np;
def pset(images,x,y,r,g,b):
	images[y][x][0]=r;
	images[y][x][1]=g;
	images[y][x][2]=b;
def hline(images,x1,y1,x2,r,g,b):
	xxx=range(x1,x2)
	try:
		for xx in xxx:
			images[y1][xx][0]=r;
			images[y1][xx][1]=g;
			images[y1][xx][2]=b;
	except:
		return 1
	return 0;
def vline(images,x1,y1,y2,r,g,b):
	yyy=range(y1,y2)
	try:
		for yy in yyy:
			images[yy][x1][0]=r;
			images[yy][x1][1]=g;
			images[yy][x1][2]=b;
	except:
		return 1
	return 0;
n=0;
nn=0;
nnn=0;
nnnn=0;
print("\033c\033[42;30m\n");
print ("XXXX");
image1=np.zeros((64,64,3),np.uint8);
nn=range(0,63);
for n in nn:
	vline(image1,n,0,64,0,255,0)
im=Image.fromarray(image1);
im.save("my.jpeg");
