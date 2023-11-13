import os 
import cv2 as cv
import numpy as np

img = cv.imread("tpic1-1.jpg")

k = cv.getStructuringElement(cv.MORPH_RECT,(2,2))

erosion = cv.erode(img,k)
erosion2 = cv.erode(erosion,k)
erosion3 = cv.erode(erosion2,k)

merge = np.hstack((img,erosion,erosion2,erosion3))
cv.imshow('Erode',merge)
cv.imwrite("eroded.jpg",erosion3)
cv.waitKey(0)
cv.destroyAllWindows()