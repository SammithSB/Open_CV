import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

img = cv2.imread(
    '/Users/sammithsbharadwaj/Downloads/documents/GitHub/Open_CV/images/FF1p2Z1VkAARG82.jpeg')
segmentor = SelfiSegmentation()
imgout = segmentor.removeBG(img, [0, 0, 0])
cv2.imwrite("images/bgremoved.jpeg", imgout)
cv2.waitKey(1)
