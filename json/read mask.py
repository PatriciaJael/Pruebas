import numpy as np
import json
import cv2

classes = {"class 1": 0, "class 2": 1, "class 3": 2}


def generate_segmentation_map(mask, selected_labels):
    file_name = mask.split('/')[4]
    id = file_name.split('_')[0]
    subset = mask.split('/')[2]
    recording = mask.split('/')[3]

    file = open(mask, 'r')
    data = json.loads(file.read())
    seg_map = np.zeros((data['imgWidth'], data['imgHeight']))

    if len(selected_labels) > 0:
        for obj in data['objects']:
            if obj['label'] in selected_labels:
                poly = np.array(obj['polygon'])
                if poly.ndim == 2:
                    rr, cc = polygon(poly[:, 0], poly[:, 1], seg_map.shape)
                    seg_map[rr, cc] = classes[obj['label']]
                else:
                    print(mask, " - empty polygon: ", obj['label'])
    else:
        for obj in data['objects']:
            poly = np.array(obj['polygon'])
            if poly.ndim == 2:
                rr, cc = polygon(poly[:, 0], poly[:, 1], seg_map.shape)
                seg_map[rr, cc] = classes[obj['label']]
            else:
                print(mask, " - empty polygon: ", obj['label'])

    target_file_name = "./annotation/" + subset + "-" + recording + "-" + id + '.png'

    cv2.imwrite(target_file_name, seg_map.T)
    return target_file_name
