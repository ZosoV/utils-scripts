import os
import cv2 
import glob
import argparse

kitti_width = 960
kitti_height = 544
dim_kitti = (kitti_width,kitti_height)


def return_parse():
    parser = argparse.ArgumentParser(description='Convert from Yolo to Kitti and resize images.')
    parser.add_argument('--img_dir', default='frames', type=str, help='directory of annotations and images')
    parser.add_argument('--output_img_dir', default='images', type=str, help='directory of saved images')
    parser.add_argument('--kitti_dir', default='labels', type=str, help='kitti annotations of resized images')

    return parser.parse_args()

def create_paths(args):
    if not os.path.exists(args.output_img_dir):
        os.makedirs(args.output_img_dir)

    if not os.path.exists(args.kitti_dir):
        os.makedirs(args.kitti_dir)

def resize_and_save(args, files_names):
    # Resize images and save
    for img_name in files_names:
        img = cv2.imread(img_name) 
        resized = cv2.resize(img, dim_kitti)    
        img_name = img_name.split('/')[-1]
        cv2.imwrite(os.path.join(args.output_img_dir,img_name),img)
        print("Saving reshape image: {}".format(os.path.join(args.output_img_dir,img_name)))

def yolo2kitti(args,file_annotation,kitti_file_name):
    kitti_line = "{} 0.00 0 0.00 {} {} {} {} 0.00 0.00 0.00 0.00 0.00 0.00 0.00"
    file_kitti = open(os.path.join(args.kitti_dir,kitti_file_name),"w+")
    print("Saving annotation: {}".format(os.path.join(args.kitti_dir,kitti_file_name))) 
    for line in file_annotation:
        line_s = line.split(" ")

        label = ""
        if (line_s[0] == "0"):
            label = "dontcare"
        elif (line_s[0] == "1"):
            label = "car"
        elif (line_s[0] == "2"):
            label = "plate"
        elif (line_s[0] == "3"):
            label = "moto"


        xmin = (float(line_s[1]) - 0.5 * float(line_s[3])) * kitti_width
        ymin = (float(line_s[2]) - 0.5 * float(line_s[4])) * kitti_height
        xmax = (float(line_s[1]) + 0.5 * float(line_s[3])) * kitti_width
        ymax = (float(line_s[2]) + 0.5 * float(line_s[4])) * kitti_height

        xmin = 0 if (xmin < 0) else xmin
        ymin = 0 if (ymin < 0) else ymin
        xmax = kitti_width if (xmax > kitti_width) else xmax
        ymax = kitti_height if (ymax > kitti_height) else ymax

        tmp_line = kitti_line.format(label,xmin,ymin,xmax,ymax)
        file_kitti.write(tmp_line + "\n")

    file_kitti.close() 

def load_save_annotation(args):
    annotation_path = os.path.join(args.img_dir,'*.txt')
    annotations = glob.glob(annotation_path) 

    for annot in annotations:
        kitti_file_name = annot.split('/')[-1]

        file_annotation = open(annot, "r")

        yolo2kitti(args,file_annotation,kitti_file_name)

        file_annotation.close() 

if __name__ == "__main__":
    args = return_parse()

    create_paths(args)

    #data_path = os.path.join(args.img_dir,'*.png') 
    #files_names = glob.glob(data_path)

    #resize_and_save(args,files_names)

    load_save_annotation(args)



#os.remove
