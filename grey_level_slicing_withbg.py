import cv2
import numpy as np

a = int(input("enter the range 1: "))
b = int(input("enter the range 2: "))

img = cv2.imread("zac.jpg",0)
x,y = img.shape
z = np.zeros((x,y))
for i in range(0,x):
    for j in range(0,y):
        if(img[i,j]>a and img[i,j]<b):
            z[i,j] = 0
        else:
            z[i,j] = img[i,j]
cv2.imshow("transformed image",z)

            
