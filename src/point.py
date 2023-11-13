import cv2 as cv
import numpy as np

img = cv.imread("R1.jpg")
imgs =cv.imread("R2.jpg")
img = cv.resize(img,(1080,1440))
imgs = cv.resize(img,(1080,1440))
tl = (240,585)    #좌상
tr = (810,585)    #우상
br = (1050,1010)  #우하
bl = (40,1010)  #좌하

cv.circle(img,tl,5,(0,0,255),-1)
cv.circle(img,tr,5,(0,0,255),-1)
cv.circle(img,bl,5,(0,0,255),-1)
cv.circle(img,br,5,(0,0,255),-1)

cv.circle(imgs,tl,5,(0,0,255),-1)
cv.circle(imgs,tr,5,(0,0,255),-1)
cv.circle(imgs,bl,5,(0,0,255),-1)
cv.circle(imgs,br,5,(0,0,255),-1)

cv.imshow("img",img)
cv.imshow("img2",imgs)
cv.waitKey(0)
cv.destroyAllWindows()