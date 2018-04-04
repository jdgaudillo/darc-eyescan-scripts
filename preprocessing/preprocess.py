import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageOps


ROOT_PATH = os.path.abspath('')
data_directory = os.path.join(ROOT_PATH, "image")
target_dir = os.path.join(ROOT_PATH, "processed_images/")
size = sys.argv[1].split(',')
size = [int(i) for i in size]
border = int(sys.argv[2])

def loadData(data_directory):
	for f in os.listdir(data_directory):
		file_names = os.path.join(data_directory, f)
		if file_names.endswith('.jpg'):
			img = cv2.imread(file_names)
			img = cv2.copyMakeBorder(img, top = border, bottom = border, left = 0, right = 0, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])
			img = cv2.resize(img,(size[0], size[1]))
			# UNCOMMENT THE NEXT LINE IF GRAYSCALE IS REQUIRED FOR PREPROCESSING.
			# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
			cv2.imwrite(target_dir + f , img)

loadData(data_directory)

