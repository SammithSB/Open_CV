# live render web cam and convert it to cartoon in real time
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()

    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(gray_img)
    blur = cv2.GaussianBlur(invert, (29, 29), 0)
    invertedBlur = cv2.bitwise_not(blur)
    sketch = cv2.divide(gray_img, invertedBlur, scale=230.0)
    cv2.imshow('frame', sketch)
    if(cv2.waitKey(1) & 0xFF == ord('p')):
        cv2.imwrite('images/cartoon_sketch.jpg', sketch)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break
cap.release()
cv2.destroyAllWindows()
