import cv2 as cv
import numpy as np


imgs = ["duplicate_vertical_stitch_2.jpg","duplicate_vertical_stitch.jpg"]
image = [cv.imread(file) for file in imgs]

height,width,channels = image[0].shape
overlap = width * 2//3
r_width = width * len(image) - overlap * (len(image))

output = np.zeros((height,r_width,channels), dtype = np.uint8)

for i in range(len(image)) :
    if i > 0 :
        output[:,i * (width - overlap):(i + 1) * (width - overlap),:] = image[i][:,overlap:,:]
else :
    output[:,i * width:(i + 1) * width, : ] = image[i]
    
cv.imshow("total",output)
cv.waitKey(0)
cv.destroyAllWindows()