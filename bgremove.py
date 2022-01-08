import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

img = cv2.imread('images/IMG-7098.jpg')
segmentor = SelfiSegmentation()
imgout = segmentor.removeBG(img, [0, 0, 0])
cv2.imwrite("images/bgremoved.jpg", imgout)
cv2.waitKey(1)
