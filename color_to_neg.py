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
def nega(b,g,r):
    row,col = b.shape
    negC1 = np.zeros((row,col),dtype=np.uint8)
    negC2 = np.zeros((row,col),dtype=np.uint8)
    negC3 = np.zeros((row,col),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negC1[i,j]= abs(b[i,j] - 255)
            negC2[i,j]= abs(g[i,j] - 255)
            negC3[i,j]= abs(r[i,j] - 255)
    return (negC1,negC2,negC3)

def merge(img,n1,n2,n3):
    row,col,chan = img.shape

    rchan1 = np.zeros((row,col,chan),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
           rchan1[i,j,0]=n1[i,j]
           rchan1[i,j,1]=n2[i,j]
           rchan1[i,j,2]=n3[i,j]
    return (rchan1)

def greyCon(b,g,r):
    row,col = b.shape
    grayChan = np.zeros((row,col),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grayChan[i,j]= r[i,j]*0.3 + g[i,j]*0.59 + b[i,j]*0.11
    return grayChan
def rotate(greyimg):
    row,col = greyimg.shape
    ri = np.zeros((col,row), dtype=np.uint8)
    for i in range(row):
        for j in range(col):
            ri[j,i] = greyimg[i,j]
    return ri        

img=cv2.imread('C:/New folder/ss.jpg')
b,g,r = channelExtraction(img)

n1,n2,n3 = nega(b,g,r)
greyimg = greyCon(b,g,r)
##rotated = rotate(greyimg)
##cv2.imshow('ro',rotated)
r = merge(img,n1,n2,n3)
cv2.imshow('r',r)


cv2.waitKey(0)
