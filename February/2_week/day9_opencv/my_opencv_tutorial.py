import cv2

img = cv2.imread('Real_Madrid_CF.svg.png')

# 이미지 표시
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('output.jpg',img)