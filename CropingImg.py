import time
import glob
import cv2
#img = cv2.imread('image.JPG')



# Number of pieces Horizontally 
CROP_W_SIZE  = 3
# Number of pieces Vertically to each Horizontal  
CROP_H_SIZE = 2
#data = "D:\Malek\Projects\stage\Croping images\images"
#categories= ["positive","negatives"]

#for category in categories:
    #path = os.path.join(data, category)
    #for img in os.listdir(data):
for img in glob.glob("D:\Malek\Projects\stage\Croping images\images\*.JPG"):
        img2= cv2.imread(img)
        img=img2
        height, width, channels = img2.shape
        for ih in range(CROP_H_SIZE ):
                for iw in range(CROP_W_SIZE ):

                            x = int(width/CROP_W_SIZE * iw)
                            y = int(height/CROP_H_SIZE * ih)
                            h = int(height / CROP_H_SIZE)
                            w = int(width / CROP_W_SIZE )
                            print(x,y,h,w)
                            z=y+h
                            f=x+w
                            img2=img2[y:z, x:f]

                            NAME = str(time.time())
                            cv2.imwrite("cropped/"+ NAME +".JPG",img2)
                            img2 = img