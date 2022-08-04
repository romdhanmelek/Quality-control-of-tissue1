import os
import time
import cv2
import glob
data = "D:\Malek\Projects\stage\Croping images\images"
for file in glob.glob("D:\Malek\Projects\stage\Croping images\images\*.JPG"):

        img= cv2.imread(file)
        print(img)

        NAME = str(time.time())
        cv2.imwrite("D:\Malek\Projects\stage\Croping images" + NAME + ".JPG", img)
