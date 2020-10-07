#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
    annotation_file = str(sys.argv[1])
    
    f = open(annotation_file, "r")

    dict_annot = {}
    labels = []

    for line in f:
        path, label = line.split(" ")
        dict_annot[label] = path
        labels.append(label)

    seen = set(labels)
    repeated = set([x for x in labels if labels.count(x) > 1])
    uniques = list(seen - repeated)

    print("Unique annotations count: {}".format(len(uniques)))

    file = open("annotation_val.txt","w+")

    chunk_unique = uniques[0:400]

    for label in chunk_unique:
        string = dict_annot[label] + " " + label
        file.write(string)

    file.close()

    file = open("annotation_train.txt","w+")

    for label in labels:
        if not (label in chunk_unique):
            string = dict_annot[label] + " " + label
            file.write(string)

    file.close()