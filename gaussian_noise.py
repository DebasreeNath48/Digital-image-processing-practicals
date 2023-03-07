import cv2
import numpy as np
img = cv2.imread('zac.jpg',0)
def noisy(img):
    noisy = np.zeros(img.shape,np.float32)
    row,col = img.shape
    mean = 0
    var = 40
    sigma = var**0.5
    gauss = np.random.normal(mean,sigma,(row,col))
    #gauss = gauss.reshape(row,col)
    noisy = img+gauss
    return noisy
new_image = noisy(img)
cv2.normalize(new_image,new_image,0,255,cv2.NORM_MINMAX,dtype=-1)
new_image = new_image.astype(np.uint8)

print(len(img.shape))#2
cv2.imshow("new image",new_image)
cv2.imshow("original",img)
