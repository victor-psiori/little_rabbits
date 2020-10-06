import numpy as np
from glob import glob
from glob import iglob
import os
import cv2
import csv
import shutil


def getFilenames(inputDir=None):
    print("Getting filenames in the directory")
    ip_filenames = glob(inputDir + "/*.png")
    filenames = []
    for f_name in ip_filenames:
        rn = f_name.split("/")[len(f_name.split("/"))-1]
        print(f"{rn}")
        filenames.append(rn)

    return filenames

def copyImagesWithNames(filenames=None, src=None, dest=None):
    """
    function copies files with given names in list ip_filenames from src to dst
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    abs_fps = []
    count = 0
    for f_name in filenames:
        # fp = glob(src)
        # ip_filename = src + "/" + f_name
        # print("filename: %s is copied to %s" %(f_name, dest))
        # shutil.copy(ip_filename, dest)
        reg_exp = src + "/images/right_trolley_cam/2020/08/**/" + f_name
        for fp in iglob(reg_exp, recursive=True):
        	count += 1
        	print(f"captured fp : {fp} for image : {count}")
        	shutil.copy(fp, dest)



if __name__ == "__main__":
    filesToCopy = getFilenames("right_trolley_images")
    copyImagesWithNames(filenames=filesToCopy, src="right_trolley_260_280_no_load", dest="right_trolley_images_originals")