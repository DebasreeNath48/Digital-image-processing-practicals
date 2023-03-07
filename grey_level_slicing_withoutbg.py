import cv2
import numpy as np
a = int(input("Enter the range 1: "))
b = int(input("Enter the range 2: "))
img = cv2.imread("zac.jpg", 0)

x, y = img.shape
z = np.zeros((x, y))

for i in range(0, x):
    for j in range(0, y):
        if img[i][j] > a and img[i][j] < b:
            z[i][j] = 255
        else:
            z[i][j] = 0
cv2.imshow("Transformed image", z)
cv2.waitKey()
cv2.destroyAllWindows()

# Enter the range 1: 150
# Enter the range 2: 2150
