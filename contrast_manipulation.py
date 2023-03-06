import cv2
def Contrast(img,contrast=255):
    contrast = int((contrast - 0)*(255-(-255))/510 + (-255))
# Change in contrast...
    if contrast != 0:
        alpha1 = float(255 * (contrast + 255)) / (255 * (255-contrast))
        gamma1 = 255 * (1 - alpha1)
        nowimg = cv2.addWeighted(img, alpha1, img, 0, gamma1)
    return nowimg


original = cv2.imread("zac.jpg")
cv2.imshow("Original", original)
contrast_img = Contrast(original,370)
cv2.imshow("contrast", contrast_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
