import cv2 as cv
import numpy as np

win_name = "scan_imgs"
save_img_path = "../imgs/perspective/"
img = cv.imread("test1.jpg")
row, cols = img.shape[:2]
pts = np.zeros((4,2), dtype= np.float32)

pts1 = np.float32([[547,473],[282,470],[948,992],[15,992]])
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

cv.circle(img,(547,473), 5,(0,0,255),-1)
cv.circle(img,(282,470), 5,(0,0,255),-1)
cv.circle(img,(948,992), 5,(0,0,255),-1)
cv.circle(img,(15,992), 5,(0,0,255), -1)

matrix = cv.getPerspectiveTransform(pts1,pts2)
result = cv.warpPerspective(img,matrix,(1100,1100))

cv.imshow("result",cv.resize(result,(800,800)))
cv.waitKey(0)