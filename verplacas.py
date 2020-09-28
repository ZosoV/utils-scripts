import fileinput
import glob
#import sys
import cv2
import os

print("ric")

os.chdir("crops/real/")
for filename in glob.glob('*.png'):
    
#    print('ric')
    print(filename)  


    image= cv2.imread(filename)
    print(image.shape[0], image.shape[1])

    image = cv2.resize(image, (320,240))


    cv2.imshow("ric",image)
    cv2.waitKey(0)
