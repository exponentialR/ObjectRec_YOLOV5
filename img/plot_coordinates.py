import os

import cv2
# import numpy as np
# import json
import glob


# txt_files = glob.glob("*.txt")
# w = os.path.dirname(__file__)
def bbox(x, y, w, h):
    x1, y1 = x - w / 2, y - h / 2
    x2, y2 = x + w / 2, y + h / 2
    return x1, y1, x2, y2


def return_img():
    clas_dict = {}
    txt_files = glob.glob('{}/**/*.txt'.format(os.path.dirname(__file__)), recursive=True)
    # print(os.getcwd())
    lst1 = []
    cl = []
    class_path = os.path.join(os.getcwd(), str('classes.txt'))
    print(class_path)
    for filename in txt_files:

        if filename == class_path:
            w = open(filename, 'r')
            for clas in w:
                lst1.append(clas)
            clas_dict['classes']= lst1
            # print(clas_dict, end= '')
            w.close()
            pass

        img = cv2.imread('%s.jpg' % filename[:-4])
        # print(img)
        dh, dw, _ = img.shape

        f = open(filename)

        # w = open()
        lines = f.readline()
        # _, x, y, w, h = map(float, lines.split(' '))

        # print(clas_dict)
        for l in lines:
            _, x, y, w, h = map(float, lines.split(' '))


            # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
            # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
            l = int((x - w / 2) * dw)
            r = int((x + w / 2) * dw)
            t = int((y - h / 2) * dh)
            b = int((y + h / 2) * dh)

            if l < 0:
                l = 0
            if r > dw - 1:
                r = dw - 1
            if t < 0:
                t = 0
            if b > dh - 1:
                b = dh - 1

            cv2.rectangle(img, (l, t), (r, b), (255, 0, 255), 2)
            cv2.imshow("With Bounding Box", img)
            cv2.imwrite("{}.png" .format(filename[:-4]), img)
            cv2.waitKey(1)


return_img()
