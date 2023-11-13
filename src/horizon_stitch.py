import cv2 as cv
import numpy as np 

save_img_path = "../imgs/stitch/"
imgs = ["duplicate_vertical_stitch_2.jpg","duplicate_vertical_stitch.jpg"]
image = [cv.imread(file)for file in imgs]

height, width, channels = image[0].shape
r_width = width * len(image)

output = np.zeros((height, r_width,channels), dtype=np.uint8)
for i in range(len(image)) :
    output[:, i * width:(i + 1) * width, :] = image[i]
    
#output = cv.resize(output,(1000,400))
cv.imshow("pano",output)
cv.waitKey(0)
cv.imwrite(f'{save_img_path}horizon_stitch.jpg', output)