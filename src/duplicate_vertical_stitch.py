import cv2 as cv
import numpy as np

imgs = ['PR15.jpg','PR14.jpg','PR13.jpg','PR12.jpg','PR11.jpg','PR10.jpg','PR9.jpg','PR8.jpg','PR7.jpg','PR6.jpg','PR5.jpg','PR4.jpg','PR3.jpg','PR2.jpg','PR1.jpg']
image = [cv.imread(file) for file in imgs]

height,width, channels = image[0].shape
overlap =  height * 1//3
r_hegith = height * len(image) - overlap *(len(image))

output = np.zeros((r_hegith, width, channels), dtype=np.uint8)

for i in range(len(image)) :
    if i > 0 :
        output[i * (height - overlap):(i + 1) * (height - overlap), :, :] = image[i][overlap:, :, :]
    else :
        output[i * height:(i + 1) * height, : ,:] = image[i]
        
#output = cv.resize(output,(500,1000))
cv.imshow("pano",output)
cv.imwrite("R_duplicate_vertical_stitch.jpg", output)
cv.waitKey(0)
cv.destoryAllWindows()
