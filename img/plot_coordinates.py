import os

import cv2
import numpy as np
import json
import glob

# txt_files = glob.glob("*.txt")
# w = os.path.dirname(__file__)
def bbox(x,y,w,h):
    x1, y1 = x-w/2, y-h/2
    x2, y2 = x+w/2, y+h/2
    return x1, y1, x2, y2

def return_img():
    lst1 = []
    txt_files = glob.glob('{}/**/*.txt'.format(os.path.dirname(__file__)), recursive=True)
    for filename in txt_files:
        img = cv2.imread('%sjpg'%filename[:-3])
        # cv2.imshow('Out', img)
        dh, dw, _ = img.shape

        f = open (filename)
        lines = f.readline()
        for l in lines:
        #
        #     # Split string to float
            _, x, y, w, h = map (float, lines.split (' '))

            # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
            # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
            l = int ((x - w / 2) * dw)
            r = int ((x + w / 2) * dw)
            t = int ((y - h / 2) * dh)
            b = int ((y + h / 2) * dh)

            if l < 0:
                l = 0
            if r > dw - 1:
                r = dw - 1
            if t < 0:
                t = 0
            if b > dh - 1:
                b = dh - 1

            cv2.rectangle (img, (l, t), (r, b), (0, 0, 255), 1)


            cv2.imwrite ("my.png", img)
            # #
            cv2.imshow ("lalala", img)
        cv2.waitKey (0)



return_img()
