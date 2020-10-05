#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
    annotation_file = str(sys.argv[1])


    f = open(annotation_file, "r")

    labels_list = []

    for line in f:
        img, label = line.split(sep=" ")
        
        labels_list.append(label)

    final_list = list(dict.fromkeys(labels_list))

    print("Not repeated: {}".format(len(final_list)))