import numpy as np
from glob import glob
import os
import cv2
import csv
import shutil
import pandas as pd
import matplotlib.pyplot as plt
import random

def copyRandomSampledFiles(no_files, inputDir=None, outputDir=None):
    # ip_filenames = glob(inputDir + "/**/*.jpg", recursive=True)
    ip_filenames = glob(inputDir + "/*.jpg", recursive=False)
    print(f"len ip_filenames : {len(ip_filenames)}")

    rand_indices = np.random.choice(len(ip_filenames), no_files, replace=False)

    if not os.path.exists(outputDir):
        os.makedirs(outputDir)

    for id in rand_indices:
        file_to_copy = ip_filenames[id]
        shutil.copy(file_to_copy, outputDir)

    op_fs = glob(outputDir + "/*.jpg")
    print(f"no files copied : {len(op_fs)}")

def pngToJpg(inputDir=None):
	ip_filenames = glob(inputDir + "/*.png")
	print(f"Loading input data : {len(ip_filenames)}")

	for f_name in ip_filenames:
		img = cv2.imread(f_name)
		op_file = f_name.split(".")[len(f_name.split("."))-2]
		op_file += ".jpg"
		# print(f"op_file: {op_file}")
		cv2.imwrite(op_file, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

	op_fs = glob(inputDir + "/*.jpg")
	print(f"total jpg files : {len(op_fs)}")


def writeFilenamesToCsv(inputDir=None, 
                        prefix="https://autocranedevdata.blob.core.windows.net/qm-200929-trolleycamright-varied-images/",
                        csv_file=None):
    ip_fs = glob(inputDir + "/**/*.jpg", recursive=True)
    print(f"total number of files: {len(ip_fs)}")
    azure_filenames = []
    for f_name in ip_fs:
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

def copyEverything(inputDir=None, outputDir=None):
	if not os.path.exists(outputDir):
		os.makedirs(outputDir)
	ip_fs = glob(inputDir + "/**/*.jpg", recursive=True)
	print(f"number of files input : {len(ip_fs)}")
	for f in ip_fs:
		shutil.copy(f, outputDir)

	op_fs = glob(outputDir + "/*.jpg")
	print(f"number of files in output : {len(op_fs)}")


if __name__=="__main__":
	# copyRandomSampledFiles(200, inputDir="input_data/unload/left_trolley", 
	# 					   outputDir="output_data/unload/left_trolley")

	# copyRandomSampledFiles(150, inputDir="input_data/unload/cabin", 
	# 					   outputDir="output_data/unload/cabin")

	# copyRandomSampledFiles(200, inputDir="input_data/unload2/right_trolley", 
	# 					   outputDir="output_data/unload2/right_trolley")

	# copyRandomSampledFiles(200, inputDir="input_data/unload2/sillbeam", 
	# 					   outputDir="output_data/unload2/sillbeam_center")

	# copyRandomSampledFiles(150, inputDir="input_data/unload2/op_cabin", 
	# 					   outputDir="output_data/unload2/cabin")

	# copyRandomSampledFiles(150, inputDir="input_data/unload3/left_trolley", 
	# 					   outputDir="output_data/unload3/left_trolley")

	# copyRandomSampledFiles(100, inputDir="input_data/unload3/right_trolley", 
	# 					   outputDir="output_data/unload3/right_trolley")

	# copyRandomSampledFiles(150, inputDir="input_data/unload3/sillbeam", 
	# 					   outputDir="output_data/unload3/sillbeam_center")

	# copyRandomSampledFiles(200, inputDir="input_data/unload3/op_cabin", 
	# 					   outputDir="output_data/unload3/cabin")

	# pngToJpg(inputDir="output_data/unload1/cabin")
	# pngToJpg(inputDir="output_data/unload/left_trolley")
	# pngToJpg(inputDir="output_data/unload/right_trolley")
	# pngToJpg(inputDir="output_data/unload/sillbeam_center")

	# pngToJpg(inputDir="output_data/unload2/cabin")
	# pngToJpg(inputDir="output_data/unload2/left_trolley")
	# pngToJpg(inputDir="output_data/unload2/right_trolley")
	# pngToJpg(inputDir="output_data/unload2/sillbeam_center")

	# pngToJpg(inputDir="output_data/unload3/cabin")
	# pngToJpg(inputDir="output_data/unload3/left_trolley")
	# pngToJpg(inputDir="output_data/unload3/right_trolley")
	# pngToJpg(inputDir="output_data/unload3/sillbeam_center")
	# prefix = "https://autocranedevdata.blob.core.windows.net/qm-2020-10-28-minicrane/"
	# writeFilenamesToCsv(inputDir="output_data/qm-2020-10-28-minicrane/cabin_cam",
 	#                      prefix=prefix,
 	#                      csv_file="cabin_cam_images.csv")

	# writeFilenamesToCsv(inputDir="output_data/qm-2020-10-28-minicrane/left_trolley_cam",
 	#                        prefix=prefix,
 	#                        csv_file="left_trolley_cam_images.csv")

	# writeFilenamesToCsv(inputDir="output_data/qm-2020-10-28-minicrane/right_trolley_cam",
 	#                        prefix=prefix,
 	#                        csv_file="right_trolley_cam_images.csv")

	# writeFilenamesToCsv(inputDir="output_data/qm-2020-10-28-minicrane/sillbeam_center_cam",
 	#                        prefix=prefix,
 	#                        csv_file="sillbeam_cam_images.csv")
 	
 	### unload4 works ###
 	# select the files
 	# copyRandomSampledFiles(250, inputDir="input_data/unload4/cabin", outputDir="output_data/unload4/cabin")
	# copyRandomSampledFiles(300, inputDir="input_data/unload4/left_trolley", outputDir="output_data/unload4/left_trolley")
	# copyRandomSampledFiles(150, inputDir="input_data/unload4/right_trolley", outputDir="output_data/unload4/right_trolley")
	# copyRandomSampledFiles(300, inputDir="input_data/unload4/sillbeam", outputDir="output_data/unload4/sillbeam")

	# convert png to jpg
	# pngToJpg(inputDir="output_data/unload4/cabin")
	# pngToJpg(inputDir="output_data/unload4/left_trolley")
	# pngToJpg(inputDir="output_data/unload4/right_trolley")
	# pngToJpg(inputDir="output_data/unload4/sillbeam")

	# fetch random samples from qm-2020-10-28-minicrane batch
	# copyRandomSampledFiles(250, inputDir="output_data/qm-2020-10-30-minicrane/cabin_cam", outputDir="output_data/unload4/cabin")
	# copyRandomSampledFiles(200, inputDir="output_data/qm-2020-10-30-minicrane/left_trolley_cam", outputDir="output_data/unload4/left_trolley")
	# copyRandomSampledFiles(50, inputDir="output_data/qm-2020-10-30-minicrane/right_trolley_cam", outputDir="output_data/unload4/right_trolley")
	# copyRandomSampledFiles(200, inputDir="output_data/qm-2020-10-30-minicrane/sillbeam_center_cam", outputDir="output_data/unload4/sillbeam")






