import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("flower.jpg",0)

def differnece_operator_horizontal(img):
    rows,cols = img.shape
    nimh = np.zeros((rows,cols),dtype = np.uint8)
    for i in range(rows):
        for j in range(cols-1):
            nimh[i,j] = img[i,j+1]-img[i,j]
    return nimh            
    
def difference_operator_vertical(img):
    rows,cols = img.shape
    nimv = np.zeros((rows,cols),dtype = np.uint8)
    for i in range(rows-1):
        for j in range(cols):
            nimv[i,j] = img[i+1,j]-img[i,j]
    return nimv
