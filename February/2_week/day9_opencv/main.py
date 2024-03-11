import cv2
img = cv2.imread('Real_Madrid_CF.svg.png')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale img',gray_img)
cv2.imshow('Original image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()