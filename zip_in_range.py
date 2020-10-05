import zlib
import zipfile
import argparse
import glob
import os

def return_parse():
    parser = argparse.ArgumentParser(description='zip in parts')
    parser.add_argument('--input-dir', default='crops', type=str, help='directory of files')
    parser.add_argument('--parts', default=3, type=int, help='number of parts')
    
    return parser.parse_args()

def compress(file_names,zip_name):
    # print("File Paths:")
    # print(file_names)

    # Select the compression mode ZIP_DEFLATED for compression
    # or zipfile.ZIP_STORED to just store the file
    compression = zipfile.ZIP_DEFLATED

    # create the zip file first parameter path/name, second mode
    zf = zipfile.ZipFile(zip_name, mode="w")

    # output path
    output_path_in_zip = zip_name.split(".")[0]
    try:
        for file_path in file_names:
            file_name = file_path.split("/")[-1]
            # Add file to the zip file
            # first parameter file to zip, second filename in zip
            zf.write(file_path, output_path_in_zip+ "/" + file_name, compress_type=compression)

    except FileNotFoundError:
        print("An error occurred")
    finally:
        # Don't forget to close the file!
        zf.close()

if __name__ == "__main__":
    args = return_parse()

    data_path = data_path = os.path.join(args.input_dir,'*.jpg') 
    files_names = glob.glob(data_path)
    step = int (len(files_names) / args.parts)

    print(len(files_names))
    for i in range(args.parts):
        if (i != args.parts - 1):
            print("Compress from {} to {}: ".format(i*step,(i+1)*step))
            compress(files_names[i*step:(i+1)*step],"data_chunck_{}.zip".format(i + 1))
        else:
            print("Compress from {} to {}: ".format(i*step,len(files_names) - 1))
            compress(files_names[i*step:len(files_names) - 1],"data_chunck_{}.zip".format(i + 1))

    # # file_names= ["test_file.txt", "test_file2.txt"]
    # # compress(file_names)