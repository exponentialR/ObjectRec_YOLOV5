import glob
import itertools
import time
from pathlib import Path
import os
import pathlib
import shutil


def copy_delete(src, des):
    txt_files = glob.glob('{}/**/*.txt'.format(src), recursive=True)
    i = 0
    for txt in txt_files:
        img_to_copy = ('%sjpg' % txt[:-3])
        try:
            if img_to_copy[:-3] == txt[:-3]:
                shutil.move(img_to_copy, des)
                shutil.move(txt, des)
            pass
        except:
            FileNotFoundError

        finally:

            i +=2
            print('Total file moved:' + str(i))


source = r'C:\Users\Research\Obj_Rec\Rename'
destination = r'C:\Users\Research\Obj_Rec\destination'
txt_files = glob.glob('{}/**/*.txt'.format(source), recursive=True)


copy_delete(source, destination)

