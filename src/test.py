import glob
import numpy as np
import cv2 as cv
import pandas as pd

img_path = "C:/Users/line/Desktop/stitch and perspective/imgs"
save_img_path = "../imgs/perspective/"

df = pd.read_csv('2023_11_10.csv')
df_c = df.copy()

df['x'] = df['x'] * 1000
df['y'] = df['y'] * 1000
df['x'] = df['x'].astype(int)
df['y'] = df['y'].astype(int)

img_list = [cv.resize(cv.imread(file),(1080,1440)) for file in glob.glob(f'{img_path}/*jpg')]

canvas_row, canvas_cols = 30000, 30000
canvas = np.zeros((canvas_row,canvas_cols,3),dtype=np.uint8) + 255

tl = (240,585)    #좌상
tr = (810,585)    #우상
br = (1050,1010)  #우하
bl = (40,1010)  #좌하
val = 1000

pts1 = np.float32([tl,tr,br,bl])
pts2 = np.float32([[0,0],[val-1,0],[val-1,val-1],[0,val-1]])

matrix = cv.getPerspectiveTransform(pts1,pts2)
crop_list = []
crop = cv.warpPerspective(img_list[1],matrix,(val,val))
for i in range(len(img_list)):
    warping = cv.warpPerspective(img_list[i], matrix,(val,val))
    crop_list.append(warping)
    y_offset = df['y'][i] + 5000
    x_offset = df['x'][i] + 5000
    
    height, width, channels= crop.shape    
    canvas[y_offset:y_offset + height, x_offset:x_offset+width] = crop_list[i]
#cv.imshow("result",canvas)
cv.imwrite("result.jpg",canvas)
cv.waitKey(0)
cv.destroyAllWindows()