import cv2
def brightness(img, brightness=255):
    brightness = int((brightness - 0)*(255-(-255))/510 + (-255))
    print(brightness)

# Change in brightness...
    if brightness != 0:
        if brightness > 0:
            shadow = brightness
            max = 255
        else:
            shadow = 0
            max = 255+brightness
        alpha = (max - shadow)/255
        gamma = shadow
        nowimg = cv2.addWeighted(img, alpha, img, 0, gamma)
    else:
        nowimg = img
    return nowimg    

original = cv2.imread("zac.jpg")
cv2.imshow("Original", original)
bright = brightness(original, 340)
cv2.imshow("Bright", bright)
cv2.waitKey(0)
cv2.destroyAllWindows()
