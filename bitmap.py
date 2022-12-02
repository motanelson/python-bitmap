#!/usr/bin/python
from PIL import Image;
import PIL ;
import numpy as np;
def pset(images,x,y,r,g,b):
	images[y][x][0]=r;
	images[y][x][1]=g;
	images[y][x][2]=b;
def hline(images,x1,y1,x2,r,g,b):
	xxx=range(x1,x2);
	try:
		for xx in xxx:
			images[y1][xx][0]=r;
			images[y1][xx][1]=g;
			images[y1][xx][2]=b;
	except:
		return 1
	return 0;
def vline(images,x1,y1,y2,r,g,b):
	yyy=range(y1,y2);
	try:
		for yy in yyy:
			images[yy][x1][0]=r;
			images[yy][x1][1]=g;
			images[yy][x1][2]=b;
	except:
		return 1
	return 0;
def boxs(images,x1,y1,x2,y2,r,g,b):
	xxx=range(x1,x2);
	yyy=range(y1,y2);
	try:
		for yy in yyy:
			for xx in xxx:
				images[yy][xx][0]=r;
				images[yy][xx][1]=g;
				images[yy][xx][2]=b;
	except:
		return 1
	return 0;
def createImg(w,h):
	return np.zeros((h,w,3),np.uint8);
def ImgSave(files,image1):
	im=Image.fromarray(image1);
	im.save(files);
def pasts(images0,images1,x1,y1,x2,y2,x,y):
	r=0;
	g=0;
	b=0;
	xxx=range(x1,x2);
	yyy=range(y1,y2);
	try:
		for yy in yyy:
			for xx in xxx:
				r=images1[yy][xx][0];
				g=images1[yy][xx][1];
				b=images1[yy][xx][2];
				images0[yy-y1+y][xx-x1+x][0]=r;
				images0[yy-y1+y][xx-x1+x][1]=g;
				images0[yy-y1+y][xx-x1+x][2]=b;
	except:
		return 1
	return 0;

n=0;
nn=0;
nnn=0;
nnnn=0;
print("\033c\033[42;30m\n");
print ("XXXX");
image1=createImg(64,64);
image2=createImg(64,64);
boxs(image1,0,0,64,64,0,255,0);
pasts(image2,image1,0,0,63,63,0,0);
ImgSave("my.jpeg",image1);