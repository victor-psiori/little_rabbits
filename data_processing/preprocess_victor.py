import numpy as np
from glob import glob
import os
import cv2


def pngToJpg(inputDir=None, outputDir=None):
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        op_file = f_name.split(".")[len(f_name.split("."))-2]
        op_file += ".jpg"
        print(f"op_file: {op_file}")
        cv2.imwrite(op_file, img)

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

def normalizeWithCv(inputDir=None, norm_type=cv2.NORM_MINMAX):
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        cv2.normalize(img, img, 0, 255, norm_type=norm_type)
        cv2.imwrite(f_name, img)
    print("Images normalized. Check the result")



if __name__ == "__main__":
    resizeImage(inputDir="inputDir", h_new=256, w_new=256)