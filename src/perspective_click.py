import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
win_name = "scan_imgs"

# insert image path in here
save_img_path = "../imgs/perspective/"
img = cv.imread("ipic1-1.jpg")
row, cols = img.shape[:2]
draw = img.copy()
pts_cnt = 0
pts = np.zeros((4,2), dtype=np.float32)

def onMouse(event,x,y,flags,params):
    global pts_cnt
    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(draw,(x,y), 3,(0,0,255), -1)
        cv.imshow(win_name, draw)
        
        pts[pts_cnt] = [x, y]
        pts_cnt += 1
        # it just show your x,y value 
        print((x,y))
        if pts_cnt == 4:
            sm = pts.sum(axis=1)
            diff = np.diff(pts, axis=1)
            tl = pts[np.argmin(sm)]
            tr = pts[np.argmin(diff)]
            br = pts[np.argmax(sm)]
            bl = pts[np.argmax(diff)]
            print(tl)
            print(tr)
            print(bl)
            print(br)
            pts1 = np.float32([tl, tr, br, bl])
            w1 = abs(br[0] - bl[0])
            w2 = abs(tr[0] - tl[0])
            h1 = abs(tr[1] - br[1])
            h2 = abs(tl[1] - bl[1])
            
            width = np.uint(max([w1,w2]))
            height = np.uint(max([h1,h2]))
            
            pts2 =np.float32([[0,0], [width -1 , 0], [width -1 , height -1 ], [0, height - 1]])    
            print(pts1)
            print(pts2)
            matrix = cv.getPerspectiveTransform(pts1,pts2)
            result = cv.warpPerspective(img, matrix, (width,height))
            
            cv.imshow("scan_imgs",cv.resize(result,(1000,1000)))
            cv.imwrite(f'{save_img_path}perspective_imgs.jpg',result)
cv.imshow(win_name,img)
cv.setMouseCallback(win_name, onMouse)
cv.waitKey(0)
cv.destroyAllWindows()