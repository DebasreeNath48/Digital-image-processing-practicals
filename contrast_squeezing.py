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
def contrast_squeezing(greyimg):
    row,col = greyimg.shape
    transformed_grey = np.zeros((row,col),dtype=np.uint8)
    m=np.min(greyimg)
    n=np.max(greyimg)
    print(m,n)
    #n=136
    #m=79
    a=0
    b=255
    for i in range(row):
        for j in range(col):
            transformed_grey[i,j] = a+((b-a)*(greyimg[i,j]-m))/(n-m)
    return transformed_grey        
            

img=cv2.imread('C:/New folder/zac.jpg')
b,g,r = channelExtraction(img)
greyimg = greyCon(b,g,r)
transformed_grey = contrast_squeezing(greyimg)
fig = plt.figure(figsize = (17, 12))

pltX = 2 #rows
pltY = 2 #cols

fig.add_subplot(pltX, pltY,1) #rows,col,index
plt.imshow(greyimg, cmap="gray")
plt.axis('off')
plt.title('grey image')

fig.add_subplot(pltX, pltY,2)
plt.imshow(transformed_grey, cmap="gray")
plt.axis('off')
plt.title('transformed grey image')

plt.show()






