import os
import cv2 
import glob
import argparse

width = 94
height = 24
dim = (width,height)


def return_parse():
    parser = argparse.ArgumentParser(description='Convert from Yolo to Kitti and resize images.')
    parser.add_argument('--img_dir', default='crops', type=str, help='directory of annotations and images')
    parser.add_argument('--output_dir', default='resize_images', type=str, help='directory of saved images')

    return parser.parse_args()

def create_paths(args):
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)

def resize_and_save(args, files_names):
    # Resize images and save
    for img_name in files_names:
        img = cv2.imread(img_name) 
        resized = cv2.resize(img, dim)    
        img_name = img_name.split('/')[-1]
        cv2.imwrite(os.path.join(args.output_dir,img_name),resized)
        print("Saving reshape image: {}".format(os.path.join(args.output_dir,img_name)))

if __name__ == "__main__":
    args = return_parse()

    create_paths(args)

    data_path = os.path.join(args.img_dir,'*.jpg') 
    files_names = glob.glob(data_path)

    resize_and_save(args,files_names)





#os.remove
