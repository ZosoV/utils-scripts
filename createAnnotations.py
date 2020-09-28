import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser(
        description='make one string of each label and then copy the images to a folder')
    parser.add_argument('annotations_file',
                        help='annotations file used for the images')
    parser.add_argument(
        'path_origin', help='path to the source folder of the images')

    return parser.parse_args()


def getFiles(path):
    files = subprocess.run(
        ["ls", path], capture_output=True, text=True).stdout.split()
    return files


def writeAnnotations(files, annotationsFile):
    txtFile = open(annotationsFile, "w")
    for item in files:
        tmp = "crops/" + item + " " + item[-10:-4] + "\n"
        txtFile.write(tmp)
    txtFile.close()


# def getNames(annotationsFile):
#     imagesNames = []
#     namesCompletes = []
#     annotationsFile = open(annotationsFile, "r")
#     idx = 0
#     for line in annotationsFile:
#         tmp = line.split()
#         imagesNames.append(tmp[0][6:])
#         tmp = str(idx).zfill(12)+"_"+tmp[1]+".png"
#         namesCompletes.append(tmp)
#         idx += 1
#     return imagesNames, namesCompletes


# def cpImages(src, dest, oriNames, destNames):
#     for i in range(len(oriNames)):
#         commad = ["cp", src+"/"+oriNames[i], dest+"/"+destNames[i]]
#         subprocess.run(commad)


if __name__ == "__main__":
    args = parse_args()
    files = getFiles(args.path_origin)
    writeAnnotations(files, args.annotations_file)
    # print(imagesNames)
    # print(namesCompletes)
