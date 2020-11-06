import numpy as np
from glob import glob
import os
import cv2
import csv
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import random

def pngToJpg(inputDir=None, outputDir=None):
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        op_file = f_name.split(".")[len(f_name.split("."))-2]
        op_file += ".jpg"
        print(f"op_file: {op_file}")
        cv2.imwrite(op_file, img)

def jpgTopng(inputDir=None):
    print("Loading input data")
    ip_filenames = glob(inputDir + "/*.jpg")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        op_file = f_name.split(".")[len(f_name.split("."))-2]
        op_file += ".png"
        # print(f"op_file: {op_file}")
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
    ip_filenames = glob(inputDir + "/*.jpg")
    dim = (w_new, h_new)
    

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        img = cv2.resize(img, dim)
        cv2.imwrite(f_name, img)

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
        ip_filepath = src + "/" + f_name
        print("filepath: %s is copied to %s" %(f_name, dest))
        shutil.copy(ip_filepath, dest)

def deleteImagesWithNames(filenames=None, inputDir=None):
    """
    delete images with from inputDir with given filenames
    """
    print(f"no of files to delete: {len(filenames)}")
    for f_name in filenames:
        ip_filepath = inputDir + "/" + f_name
        # print(f"filepath: %s is deleted")
        os.remove(ip_filepath)

def renameAnnotatedImage(inputDir=None):
    print("Renaming annotated image file names")
    ip_filenames = glob(inputDir + "/*.png")

    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        rn = f_name.split('_annotate')[len(f_name.split('_annotate')) - 2]
        rn = rn + ".png"
        print("File will be renamed to %s " %rn)
        cv2.imwrite(rn, img)

def getFilenames(inputDir=None, extn=".png"):
    print("Getting filenames in the directory")
    # ip_filenames = glob(inputDir + "/*.png")
    ip_filenames = glob(inputDir + "/*" + extn)
    filenames = []
    for f_name in ip_filenames:
        rn = f_name.split("/")[len(f_name.split("/"))-1]
        # print(f"{rn} will be copied")
        filenames.append(rn)

    return filenames

def cropAndSaveImage(x=0, y=0, w=256, h=256, inputDir=None):
    print("ROI containing the truck and grapple would be cropped")
    ip_filenames = glob(inputDir + "/*.png")
    for f_name in ip_filenames:
        img = cv2.imread(f_name)
        img = img[y:y+h, x:x+w]
        cv2.imwrite(f_name, img)

def createClassificationAnnotationData(inputDir=None, csv_dest=None):
    filenames = getFilenames(inputDir=inputDir, extn=".png")
    no_files = len(filenames)
    print(f"no files : {no_files}")
    labels_short = np.zeros(no_files)
    lables_df = pd.DataFrame({'name': filenames,
                              'wood_type': labels_short})
    lables_df.to_csv(csv_dest)

def copyRandomSampledFiles(no_files, inputDir=None, outputDir=None):
    ip_filenames = glob(inputDir + "/*.png")
    print(f"len ip_filenames : {len(ip_filenames)}")

    rand_indices = np.random.choice(len(ip_filenames), no_files)

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for id in rand_indices:
        file_to_copy = ip_filenames[id]
        shutil.copy(file_to_copy, outputDir)

def deleteRandomFiles(no_files, inputDir):
    ip_filenames = glob(inputDir + "/*.png")
    print(f"total ip_filenames before del: {len(ip_filenames)}")

    rand_indices = np.random.choice(len(ip_filenames), no_files, replace=False)
    for id in rand_indices:
        file_to_del = ip_filenames[id]
        os.remove(file_to_del)

    ip_filenames = glob(inputDir + "/*.png")
    print(f"total ip_filenames after del: {len(ip_filenames)}")

if __name__ == "__main__":
    # prefix = "https://autocranedevdata.blob.core.windows.net/trolley-cam-29-09-20/"
    # prefix = "https://autocranedevdata.blob.core.windows.net/qm-200929-trolleycamright-varied-images/2020-08-21T14_58_09_262Z.jpg"
    # pngToJpg(inputDir="../../trolleyCamUnet_1471/trolley_cam_woodpiles")
    # rotateImage(inputDir="trolley_cam_rotate_left_90_pilearea", direction="right")
    # writeFilenamesToCsv(inputDir="trolley_cam_woodpiles", csv_file="azure_filepaths.csv")
    # printNumberOfLines(csv_file="azura_filepaths.csv")
    # rotateImage(inputDir="rotateMe_trolley_cam", direction="left")
    # file_names = getFilenames(inputDir="wood_classifier/good_label")
    # jpg_files = []
    # for f in file_names:
    #     jpg_f = f.split(".")[len(f.split(".")) - 2] + ".jpg"
    #     jpg_files.append(jpg_f)

    # copyImagesWithNames(filenames=jpg_files, src="wood_classifier/trolley_cam_876/images", dest="wood_classifier/good_images")
    # createClassificationAnnotationData(inputDir="wood_classifier/right_trolley_images", csv_dest='wood_classifier/short_wood.csv')
    # labels_df = pd.read_csv('wood_classifier/short_wood.csv')
    # print(f"labels_df head : {labels_df.head()}")
    # good_image_filenames = getFilenames(inputDir="wood_classifier/good_images", extn=".jpg")
    # for f in good_image_filenames:
    #     print(f"{f}")
    # print(f"good_image_filenames : {good_image_filenames}")
    # createClassificationAnnotationData(inputDir="wood_classifier/good_images", 
    #                                    csv_dest='wood_classifier/good_images.csv')
    # tot_good_df = pd.read_csv('wood_classifier/good_images.csv')

    # new_df = pd.DataFrame({'name': good_png_names,
    #                        'wood_type': np.ones(len(good_png_names))})
    # tot_good_df.update(new_df)
    # tot_good_df = tot_good_df.drop(['Unnamed: 0'], axis=1)
    # tot_good_df.to_csv('wood_classifier/final_good_images.csv')
    # # foo_df = pd.read_csv('wood_classifier/final_good_images.csv')
    # print(f"foo_df : {tot_good_df.head()}")
    # df_shortwood = pd.read_csv("wood_classifier/short_wood.csv")
    # print(f"df_shortwood head : {df_shortwood.head()}")
    # df_good = pd.read_csv("wood_classifier/final_good_images.csv")
    # print(f"df_good head : {df_good.head()}" )

    # combined_df = [df_shortwood, df_good]
    # df_result = pd.concat(combined_df)
    # index = df_result.index
    # print(f"df_result rows: {len(index)}")
    # print(f"df_result head : {df_result.head()}")
    # df_result = df_result.drop(['Unnamed: 0'], axis=1)
    # df_result.to_csv("wood_classifier/combined_images.csv")
    # resizeImage(inputDir="wood_classifier/good_images")
    # resizeImage(inputDir="wood_classifier/good_labels")
    # img = cv2.imread("right_trolley_labels/2020-08-24T14_48_47_847Z.png")
    # fig = plt.figure()
    # plt.imshow(img)
    # cv2.imshow('blacky', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # labels = getFilenames(inputDir="wood_classifier/trolley_images", extn=".png")
    # copyImagesWithNames(filenames=labels, src="wood_classifier/good_labels", dest="wood_classifier/trolley_labels")
    # createClassificationAnnotationData(inputDir="wood_classifier/trolley_labels", csv_dest="wood_classifier/trolley_labels.csv")
    # createClassificationAnnotationData(inputDir="right_trolley_labels", csv_dest="right_trolley_labels.csv")
    # jpgTopng(inputDir="/Users/victorgeorge/Downloads/trainingtrailer_trolleycam_500/images")
    # ip_fs = getFilenames(inputDir="wood_classifier/trainingtrailer_labels")
    # copyImagesWithNames(filenames=ip_fs, 
    #                     src="/Users/victorgeorge/Downloads/trainingtrailer_trolleycam_500/images",
    #                     dest="wood_classifier/trainingtrailer_images")
    # createClassificationAnnotationData(inputDir="wood_classifier/trainingtrailer_images", 
    #                                    csv_dest="wood_classifier/trainingtrailer.csv")
    # resizeImage(inputDir="wood_classifier/trainingtrailer_images", h_new=256, w_new=256)
    # resizeImage(inputDir="wood_classifier/trainingtrailer_labels", h_new=256, w_new=256)
    # resizeImage(inputDir="wood_classifier/trolley_test_images", h_new=256, w_new=256)
    # ip_fs = getFilenames(inputDir="wood_classifier/trainingtrailer_images")
    # deleteImagesWithNames(filenames=ip_fs, inputDir="wood_classifier/trolley_test_images")
    # deleteRandomFiles(200, inputDir="wood_classifier/trolley_test_images")
    resizeImage(inputDir="inputDir", h_new=256, w_new=256)






