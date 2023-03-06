import cv2
import numpy as np
import matplotlib.pyplot as plt

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

def logtransformation(b,g,r):
    row,col = b.shape
    transformedImage = np.zeros((row,col,3),dtype=np.uint8)
    max_pixel_blue = np.max(b)
    max_pixel_green = np.max(g)
    max_pixel_red = np.max(r)
    c1  = 255/np.log(1+max_pixel_blue)
    c2  = 255/np.log(1+max_pixel_green)
    c3  = 255/np.log(1+max_pixel_red)

    for i in range(row):
        for j in range(col):
            transformedImage[i,j,0] = round(c1 * np.log(1+b[i,j]))
            transformedImage[i,j,1] = round(c2 * np.log(1+g[i,j]))
            transformedImage[i,j,2] = round(c3 * np.log(1+r[i,j]))
    return transformedImage

def creatergbimage(b,g,r):
    row,col = b.shape
    rgbimg=np.zeros((row,col,3),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            rgbimg[i,j,0] = r[i,j]
            rgbimg[i,j,1] = g[i,j]
            rgbimg[i,j,2] = b[i,j]
    return rgbimg            
    

img=cv2.imread('C:/New folder/ss.jpg')
b,g,r = channelExtraction(img)
colimg = logtransformation(b,g,r)
rgb=creatergbimage(r,g,b)
lb,lg,lr = channelExtraction(colimg)
rgb_log_img = creatergbimage(lb,lg,lr)

fig = plt.figure(figsize = (17, 12))

pltX = 2 #rows
pltY = 2 #cols

fig.add_subplot(pltX, pltY,1) #rows,col,index
plt.imshow(rgb)
plt.axis('off')
plt.title('rgb image')

fig.add_subplot(pltX, pltY,2)
plt.imshow(rgb_log_img)
plt.axis('off')
plt.title('rgb log transformed image for color')

plt.show()

