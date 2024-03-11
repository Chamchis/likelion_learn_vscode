import cv2

img = cv2.imread('Real_Madrid_CF.svg.png')

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(image=gray_img,threshold1=100,threshold2=200)
cv2.imshow('Edge Detection Image',edges)
cv2.waitKey(0)
cv2.destroyWindow