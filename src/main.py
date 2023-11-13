import numpy as np
import cv2 as cv
import sys
import os
import fnmatch

points=[]
height, width, channels = 0, 0, 0
# this function can setpoints vector and display vector value
def check_vector(event,x,y,flag,params):
    global points
    global image
    # mouse left button click -> point check
    if event == cv.EVENT_LBUTTONDOWN :
        points.append((x,y))
        print(points)
        cv.circle(image,(x,y),3,(0,0,255),-1)
        if len(points) > 4:
            print("please select 4 vectors")
            sys.exit()
    # mouse right button click -> system close
    elif event == cv.EVENT_RBUTTONDOWN :
        sys.exit()

def perspective(image):
        #insert vector in here
    tl = (240,585)    #Top Left
    tr = (810,585)    #Top Right
    br = (1050,1010)  #Bottom Right
    bl = (40,1010)    #Bottom Left
    val = 1100        # val == maxium size 
    pts1 = np.float32([tl,tr,br,bl])
    pts2 = np.float32([0,0],[val-1,0],[val-1,val-1],[0,val-1]) # val - 1's mean python list start [0]
    
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    result = cv.warpPerspective(image,matrix,(1100,1100))
    cv.imshow("perspective",result)

def duplicate_vertical_stitch(image):
    overlap = height * 1//3
    r_height = height * len(image) - overlap *(len(image))
    
    output = np.zeros((r_height,widht,channels), dtype= np.uint8)
    
    for i in range(len(image)):
        if i > 0:
            output[i * (height - overlap) : (i + 1) * (height - overlap), : ,:] = image[i][overlap:,:,:]
        else :
            output[i * height:(i + 1) * height, : ,:] = image[i]
            
    cv.imshow("vetical_stitch",output)
    
def duplicate_horizon_stitch(image):
    overlap = height * 2//3
    r_width = height * len(image) - overlap * (len(image))
    
    output = np.zeros((height,r_width,channels), dtype=np.uint8)
    
    for i in range(len(image)):
        if i > 0:
            output[:,i * (width - overlap):(i + 1) * (width - overlap),:] = image[i][:,overlap,:]
        else :
            output[:,width:(i +1) * width,:] = image[i]
    
    cv.imshow("horizon_stitch",output)
    
if __name__ == "__main__"  :
    # insert image_path in here
    img_path = ["01.jpg","02.jpg",'03.jpg']
    image = [cv.imread(file)for file in img_path]

    row, cols = image[0].shape[:2]
    height, width, channels = image[0].shape[:3]
    
    cv.namedWindow("image")
    cv.setMouseCallback("image",check_vector)
    
    while True:
        cv.imshow("image",image[0])
        key = cv.waitKey(1)
        if len(points) == 4:
            break 
        
    check_vector(image[0])
    perspective(image)
    duplicate_vertical_stitch(image)
    
    cv.waitKey(0)
    cv.destroyAllWindows()
'''    
    for filename in image:
        if fnmatch.fnmatch(filename,'090_*.jpg'):
            duplicate_horizon_stitch(image[0])
        elif fnmatch.fnmatch(filename,'270_*.jpg'):
            duplicate_horizon_stitch(image[0])
        else : 
            duplicate_vertical_stitch(image[0])
        
'''    