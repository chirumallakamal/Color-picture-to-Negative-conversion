import cv2
import numpy as np

Img=cv2.imread('1.jpg');
cv2.imshow('original Image',Img);
Red_Plane=Img[:,:,2];
cv2.imshow('Red Plane Image',Red_Plane);
r,c=Red_Plane.shape;
op=np.zeros((r,c),dtype=np.uint8);
for i in range(0,r-2):
    for j in range(0,c-2):
        partimg=-1*Red_Plane[i,j]
        op[i,j]=partimg;
cv2.imshow('Image Negative',op);
cv2.waitKey(0)
