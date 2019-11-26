import cv2
import os
# import numpy as np
inputDir = r'/Users/mitevpi/Google Drive/Work/010_Project Files/191120_DaylightGAN/Data/daylight-train/input'
outputDir = r'/Users/mitevpi/Google Drive/Work/010_Project Files/191120_DaylightGAN/Data/daylight-train/merged'

counter = 0
directory = inputDir
for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        filePath = os.path.join(directory, filename)
        filePathB = filePath.replace("in-", "out-")
        filePathB = filePathB.replace("input", "output")
        im1 = cv2.imread(filePath)
        im2 = cv2.imread(filePathB)
        im_v = cv2.hconcat([im1, im2])
        merged_path = outputDir + str(counter) + ".jpg"
        cv2.imwrite(merged_path, im_v)
        print(merged_path)
        counter = counter + 1
    else:
        continue