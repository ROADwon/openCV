import cv2 as cv
import numpy as np

win_name = "scan_imgs"
save_img_path = "../imgs/perspective/"
img = cv.imread("R1.jpg")
img = cv.resize(img,(1080,1440))
row, cols = img.shape[:2]
pts = np.zeros((4,2), dtype= np.float32)
tl = (240,585)    #좌상
tr = (810,585)    #우상
br = (1050,1010)  #우하
bl = (40,1010)  #좌하
val = 1100
pts1 = np.float32([tl,tr,br,bl])
pts2 = np.float32([[0,0], [val-1,0],[val-1,val-1], [0,val-1]])
#pts2 = np.float32([0,0],[0,1000], [1000,0],[1000,1000])
#cv.circle(img,(380,430), 5,(0,0,255),-1)
#cv.circle(img,(575,430), 5,(0,0,255),-1)
#cv.circle(img,(835,800), 5,(0,0,255),-1)
#cv.circle(img,(40,800), 3,(0,0,255), -1)

matrix = cv.getPerspectiveTransform(pts1,pts2)
result = cv.warpPerspective(img,matrix,(1100,1100))
#result = cv.rotate(result,cv.ROTATE_180)
#result = cv.rotate(result,cv.ROTATE_90_COUNTERCLOCKWISE)
#cv.imshow("result",cv.resize(result,(800,800)))
cv.imwrite(f'{save_img_path}PR1.jpg',result)
cv.waitKey(0)