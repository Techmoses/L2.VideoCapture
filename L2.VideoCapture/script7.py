import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#print(img)
#img[200:300,100:300]=255,0,0

cv2.line(img,(0,0),(300,300),(0,255,0),3)

cv2.imshow("Image",img)

cv2.waitKey(0)
