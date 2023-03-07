import cv2
import numpy as np
img = cv2.imread("zac.jpg",0)

row,col = img.shape

binary = np.zeros((row,col),dtype = np.uint8)

for i in range(row):
    for j in range(col):
        if img[i,j] > 150:
            binary[i,j] = 255
        else:
            binary[i,j] = 0
cv2.imshow("original grey scale image",img)
cv2.imshow("binary image",binary)
