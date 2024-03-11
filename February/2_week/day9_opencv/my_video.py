import cv2

cap = cv2.VideoCapture('Sample_Video.mp4')
img_bool = True
while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image=gray,threshold1=100,threshold2=200)
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.waitKey(1) == ord('a'):
        img_bool = ~img_bool
    
    if img_bool:
        cv2.imshow('frame',gray)
    else:
        cv2.imshow('frame',edges)

cap.release()
cv2.destroyWindow()