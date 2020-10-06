#!/usr/bin/env python
import sys
import re

if __name__ == "__main__":
    train_file = str(sys.argv[1])
    val_file = str(sys.argv[2])


    f = open(train_file, "r")

    train_list = []

    for line in f:
        img, label = line.split(sep=" ")
        
        train_list.append(label)

    final_train_list = list(dict.fromkeys(train_list))

    print("Not repeated: {}".format(len(final_list)))

    f = open(val_file, "r")

    val_list = []

    for line in f:
        img, label = line.split(sep=" ")
        
        val_list.append(label)

    final_val_list = list(dict.fromkeys(val_list))

    repeated = set(final_val_list) & set(final_val_list)

    print("Not repeated in val: {}".format(len(val_list) - len(repeated)))