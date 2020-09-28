#!/usr/bin/env python
import sys
import shutil
import os

if __name__ == "__main__":
    annotation_file = str(sys.argv[1])

    if not os.path.exists("correct_images"):
        os.makedirs("correct_images")

    f = open(annotation_file, "r")
    for line in f:
        img_route, label = line.split(sep=" ")
        
        img_name = img_route.split("/")[-1]

        print( "Moving from {} to {}".format(img_route,os.path.join("correct_images",img_name)))
        shutil.move(img_route,os.path.join("correct_images",img_name))
        
