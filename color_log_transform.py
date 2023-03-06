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
def greyCon(b,g,r):
    row,col = b.shape
    grayChan = np.zeros((row,col),dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            grayChan[i,j]= r[i,j]*0.3 + g[i,j]*0.59 + b[i,j]*0.11
    return grayChan

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
            
    

img=cv2.imread('C:/New folder/ss.jpg')
b,g,r = channelExtraction(img)
colimg = logtransformation(b,g,r)

fig = plt.figure(figsize = (17, 12))

pltX = 2 #rows
pltY = 2 #cols

fig.add_subplot(pltX, pltY,1) #rows,col,index
plt.imshow(img)
plt.axis('off')
plt.title('normal image')

fig.add_subplot(pltX, pltY,2)
plt.imshow(colimg)
plt.axis('off')
plt.title('log transformed image for color')

plt.show()

