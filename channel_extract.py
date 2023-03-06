import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def channelExtraction(img):
    row,col,chan = img.shape

    rchan = np.zeros((row,col),dtype=np.int8)
    gchan = np.zeros((row,col),dtype=np.int8)
    bchan = np.zeros((row,col),dtype=np.int8)

    m=0
    for i in img:
        n=0
        for j in i:
            r,g,b=j
            rchan[m,n]=r
            gchan[m,n]=g
            bchan[m,n]=b
            n=n+1
        m=m+1
    return (bchan,gchan,rchan)
img = mpimg.imread("flower.jpg")
b,g,r = channelExtraction(img)

fig = plt.figure(figsize=(16, 10))
plt_x = 1
plt_y = 4
fig.add_subplot(plt_x, plt_y, 1)
plt.imshow(img)
plt.axis("off")
plt.title("original image")

fig.add_subplot(plt_x, plt_y, 2)
plt.imshow(r)
plt.axis("off")
plt.title("r channel image")

fig.add_subplot(plt_x, plt_y, 3)
plt.imshow(g)
plt.axis("off")
plt.title("g channel image")

fig.add_subplot(plt_x, plt_y, 4)
plt.imshow(b)
plt.axis("off")
plt.title("b channel image")
plt.show()



