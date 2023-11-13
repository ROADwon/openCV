import numpy as np
import cv2 as cv

img = cv.imread('L1.jpg')
img = cv.resize(img,(1080,1440))
pts = np.zeros((4,2),dtype= np.float32)
pts_cnt = 0
def onMouse(event,x,y,flags,params):
    global pts_cnt
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(img,(x,y),3,(0,0,255),-1)
        cv.imshow("result",img)
        
        pts[pts_cnt] = [x,y]
        print((x,y))
cv.imshow("result",img)
cv.setMouseCallback("result",onMouse)
cv.waitKey(0)
cv.destroyAllWindows()

        