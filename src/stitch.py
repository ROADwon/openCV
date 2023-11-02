import cv2 as cv
import numpy as np
import sys
import os 

# insert_imgs_path_in_here
imgs = ['01.jpg','02.jpg','03.jpg','04.jpg','05.jpg','06.jpg']
img = []
save_img_path = "../imgs/stitch/"

for i in range(len(imgs)):
    img.append(cv.imread(imgs[i]))
    img[i] = cv.resize(img[i],(0,0), fx=.7,fy=.7)
    
    if imgs is None : 
        print("image Load Failed System Closed")
        sys.exit()
    
stitcher = cv.Stitcher_create()
stitcher.setWaveCorrection(cv.detail.WAVE_CORRECT_AUTO)
    
(dummy, output) =stitcher.stitch(img)
print(output)
print(dummy)
    
if dummy != cv.Stitcher_OK:
    print("stitching Failed")
    sys.exit()
else :
    print("your panorama image is ready to show")
        
cv.imshow('final result', cv.resize(output,(900,900)))
cv.waitKey(0)
cv.imwrite(f'{save_img_path}stitch.jpg',output)
        
    