import numpy as np
from glob import glob
import os
import cv2
import csv
import shutil

def pngToJpg(inputDir=None, outputDir=None):
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        op_file = f_name.split(".")[len(f_name.split("."))-2]
        op_file += ".jpg"
        print(f"op_file: {op_file}")
        cv2.imwrite(op_file, img)

def writeFilenamesToCsv(inputDir=None, 
                        prefix="https://autocranedevdata.blob.core.windows.net/qm-200929-trolleycamright-varied-images/",
                        csv_file=None):
    ip_filenames_1 = glob(inputDir + "/*.jpg")
    azure_filenames = []
    for f_name in ip_filenames_1:
        rel_name = f_name.split("/")[len(f_name.split("/"))-1]
        azure_fp = prefix + rel_name
        print("relevant name : %s " %(azure_fp))
        azure_filenames.append(azure_fp)

    print("total number of azure files : %d " %len(azure_filenames))
    with open(csv_file, 'a+') as csv_f:
        writer = csv.writer(csv_f, dialect='excel')
        for f_name in azure_filenames:
            writer.writerow([f_name,])
    csv_f.close()

def printNumberOfLines(csv_file=None):
    with open(csv_file, 'r') as csv_f:
        reader = csv.reader(csv_f)
        lines = len(list(reader))
        print("Number of rows in csv file : %d " %lines)

def resizeImage(inputDir="inputDir", h_new=256, w_new=256):
    # if os.path.exists(inputDir + "/*.DS_Store"):
    #     os.remove(inputDir + "/.DS_Store")
    #     print("Removed .DStore file")
    # else:
    #     print(".DStore file doesn't exist")
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.png")
    dim = (w_new, h_new)
    

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        print(f"Initial size : {img.shape}")
        img = cv2.resize(img, dim)
        cv2.imwrite(f_name, img)
        print(f"New size : {img.shape}")

def rotateImage(inputDir=None, direction=None):
    print("Let's do rotation")
    ip_filenames = glob(inputDir + "/*.png")
    print("Total number of files to process: %d " %len(ip_filenames))

    for f_name in ip_filenames:
        print("Rotating image %s " %f_name)
        img = cv2.imread(f_name)
        if (direction == "left"):
            img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif (direction == "right"):
            img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        #write back the rotated images
        cv2.imwrite(f_name, img)

def copyImagesWithNames(filenames=None, src=None, dest=None):
    """
    function copies files with given names in list ip_filenames from src to dst
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for f_name in filenames:
        ip_filename = src + "/" + f_name
        print("filename: %s is copied to %s" %(f_name, dest))
        shutil.copy(ip_filename, dest)

def renameAnnotatedImage(inputDir=None):
    print("Renaming annotated image file names")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        rn = f_name.split('_annotate')[len(f_name.split('_annotate')) - 2]
        rn = rn + ".png"
        print("File will be renamed to %s " %rn)
        cv2.imwrite(rn, img)

def getFilenames(inputDir=None):
    print("Getting filenames in the directory")
    ip_filenames = glob(inputDir + "/*.png")
    filenames = []
    for f_name in ip_filenames:
        rn = f_name.split("/")[len(f_name.split("/"))-1]
        print(f"{rn} will be copied")
        filenames.append(rn)

    return filenames



if __name__ == "__main__":
    # prefix = "https://autocranedevdata.blob.core.windows.net/trolley-cam-29-09-20/"
    # prefix = "https://autocranedevdata.blob.core.windows.net/qm-200929-trolleycamright-varied-images/2020-08-21T14_58_09_262Z.jpg"
    # pngToJpg(inputDir="../../trolleyCamUnet_1471/trolley_cam_woodpiles")
    # rotateImage(inputDir="trolley_cam_rotate_left_90_pilearea", direction="right")
    # writeFilenamesToCsv(inputDir="trolley_cam_woodpiles", csv_file="azura_filepaths.csv")
    # writeFilenamesToCsv(inputDir="trolley_cam_truckunload", csv_file="azura_filepaths.csv")
    # printNumberOfLines(csv_file="azura_filepaths.csv")
    # rotateImage(inputDir="rotateMe_trolley_cam", direction="left")
    # resizeImage(inputDir="right_trolley_Paint")
    # renameAnnotatedImage(inputDir="right_trolley_labels")
    filesToCopy = getFilenames("right_trolley_labels")
    copyImagesWithNames(filenames=filesToCopy, src="right_trolley_Paint", dest="right_trolley_images_inputs")
    