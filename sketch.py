import cv2
image = cv2.imread("images/sam.jpeg")

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_img)
blur = cv2.GaussianBlur(invert, (29, 29), 0)
invertedBlur = cv2.bitwise_not(blur)
sketch = cv2.divide(gray_img, invertedBlur, scale=230.0)
cv2.imshow('gray_img', gray_img)
cv2.imshow('invert', invert)
cv2.imshow('blur', blur)
cv2.imshow('invertedBlur', invertedBlur)
cv2.waitKey(0)
cv2.imwrite("images/sketch1.png", sketch)
