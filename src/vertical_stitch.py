import cv2 as cv
import numpy as np

save_img_path = "../imgs/stitch/"
imgs = ['test1.jpg','test2.jpg','test3.jpg']
image = [cv.imread(file) for file in imgs]

height, width, channels = image[0].shape
r_height = height * len(image)
output = np.zeros((r_height,width,channels),dtype=np.uint8)
for i in range(len(image)) :
    output[i * height:(i + 1) * height, : ,:] = image[i]

output = cv.resize(output,(400,1000))
cv.imshow("pano",output)
cv.waitKey(0)
cv.imwrite(f'{save_img_path}vertical_stitch.jpg',output)