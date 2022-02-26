import os
import cv2
import json
import numpy as np

source_folder = os.path.join(os.getcwd(), "images")
json_path = "C:/Users/Jael/Desktop/Mapas de segmentacion"
count = 0
file_bbs = {}
MASK_WIDTH = 256
MASK_HEIGHT = 256

# Read JSON file
with open(json_path) as f:
    data = json.load(f)


def add_to_dict(data, itr, key, count):
    try:
        x_points = data[itr]["regions"][count]["shape_attributes"]["all_points_x"]
        y_points = data[itr]["regions"][count]["shape_attributes"]["all_points_y"]
    except:
        print("No BB. Skipping", key)
        return
    all_points = []
    for i, x in enumerate(x_points):
        all_points.append([x, y_points[i]])

    file_bbs[key] = all_points


for itr in data:
    file_name_json = data[itr]["filename"]
    sub_count = 0

    if len(data[itr]["filename"]) > 1:
        for _ in range(len(data[itr]["regions"])):
            key = file_name_json[:-4] + "*" + str(sub_count + 1)
            add_to_dict(data, itr, key, sub_count)
            sub_count += 1
    else:
        add_to_dict(data, itr, file_name_json[:-4], 0)

print("\nDict size: ", len(file_bbs))

for file_name in os.listdir(source_folder):
    to_save_folder = os.path.join(source_folder, file_name[:-4])
    image_folder = os.path.join(to_save_folder, "images")
    mask_folder = os.path.join(to_save_folder, "masks")
    curr_img = os.path.join(source_folder, file_name)

    os.mkdir(to_save_folder)
    os.mkdir(image_folder)
    os.mkdir(mask_folder)
    os.rename(curr_img, os.path.join(image_folder, file_name))

for itr in file_bbs:
    num_masks = itr.split("*")
    to_save_folder = os.path.join(source_folder, num_masks[0])
    mask_folder = os.path.join(to_save_folder, "masks")
    mask = np.zeros((MASK_WIDTH, MASK_HEIGHT))
    try:
        arr = np.array(file_bbs[itr])
    except:
        print("Not found:", itr)
        continue
    count += 1
    cv2.fillPoly(mask, [arr], color=255)
