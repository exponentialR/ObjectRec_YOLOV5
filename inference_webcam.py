import time

import cv2

import numpy as np
import torch


def extract_bounding_box(frame, path):
    model = torch.hub.load('ultralytics/yolov5', 'custom', path)  # default
    detect_obj = model(frame[..., ::-1])
    results = detect_obj.pandas().xyxy[0].to_dict(orient='records')
    for result in results:
        Stacked_bboxx = np.array(
            [[int(result['xmin']), int(result['ymin']), int(result['xmax']), int(result['ymax'])] for result in
             results]).flatten() if result['class'] == 'Stacked_Books' else np.zeros(4)
        Mug_bboxx = np.array(
            [[int(result['xmin']), int(result['ymin']), int(result['xmax']), int(result['ymax'])] for result in
             results]).flatten() if result['class'] == 'Mug' else np.zeros(4)
        Book_bboxx = np.array(
            [[int(result['xmin']), int(result['ymin']), int(result['xmax']), int(result['ymax'])] for result in
             results]).flatten() if result['class'] == 'Book' else np.zeros(4)
        Mugs_bboxx = np.array(
            [[int(result['xmin']), int(result['ymin']), int(result['xmax']), int(result['ymax'])] for result in
             results]).flatten() if result['class'] == 'Mugs' else np.zeros(4)
        return np.concatenate([Stacked_bboxx, Mug_bboxx, Book_bboxx, Mugs_bboxx])


cam = cv2.VideoCapture(0)
path = r'C:\Users\Research\Obj_Rec\best.pt'
while True:
    _, image = cam.read()
    time.sleep(2.0)
    keypoints = extract_bounding_box(image, path)
    print(keypoints)
    # cv2.rectangle(img, (l, t), (r, b), (255, 0, 255), 2)
    cv2.imshow('out', image)

