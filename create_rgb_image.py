import cv2
import numpy as np
def channelExtraction(img):
    row,col,chan = img.shape

    rchan = np.zeros((row,col),dtype=np.uint8)
    gchan = np.zeros((row,col),dtype=np.uint8)
    bchan = np.zeros((row,col),dtype=np.uint8)

    for i,row in enumerate(img):
        for j,col in enumerate(row):
            r,g,b=col
            rchan[i,j]=r
            gchan[i,j]=g
            bchan[i,j]=b
       
    return (bchan,gchan,rchan)

def creatergbimage(b,g,r,img):
    row,col,chan = img.shape
    rgbimg=np.zeros((row,col,chan),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rgbimg[i,j,0] = r[i,j]
            rgbimg[i,j,1] = g[i,j]
            rgbimg[i,j,2] = b[i,j]
    return rgbimg
img=cv2.imread('C:/New folder/ss.jpg')
b,g,r = channelExtraction(img)
rgb=creatergbimage(b,g,r,img)
cv2.imshow('rgbimg',rgb)
cv2.waitKey(0)
