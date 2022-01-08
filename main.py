"""
We are trying to build a background removal app and the modules used here are cvzone and mediapipe.

Import the SelfiSegmentation from cvzone.SelfiSegmentationModule.

First start capturing live camera feed and set height and weight of output.

We create a SelfiSegmenation object and that removes the background from the image, we can set what colors we want to replace beckgropund with too.

cv.CAP_PROP_FPS is used to get higher frame rates than usual, max you can set it to is 60.

Now we are adding different backgrounds for our foreground. For that we create a list, read all the image names and append it from the folder.

a and d keys are used to go forward and backward for different backgrounds.
"""
import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
cap.set(cv2.CAP_PROP_FPS, 60)
segmentor = SelfiSegmentation()
fps = cvzone.FPS()
imBG = cv2.imread("static/banni_bandhugale.jpg")
listimg = os.listdir("static")
print(listimg)
imgList = []
for i in listimg:
    img = cv2.imread(f'static/{i}')
    imgList.append(img)

imgIndex = 0
while True:
    success, img = cap.read()
    imgOut = segmentor.removeBG(img, imgList[imgIndex], threshold=0.85)
    imgStacked = cvzone.stackImages([img, imgOut], 2, 1)
    _, imgStacked = fps.update(imgStacked)
    print(imgIndex)
    cv2.imshow("image", imgStacked)
    key = cv2.waitKey(1)
    if key == ord('p'):
        if imgIndex > 0:
            imgIndex -= 1
    elif key == ord('n'):
        if imgIndex < len(imgList)-1:
            imgIndex += 1
    elif key == ord('q'):
        break
