import os
import pathlib
from pathlib import Path
# current = str(pathlib.Path().resolve())
# path = current + str('\img')
# os.chdir(path)
# files = os.listdir(path)

import argparse


parser = argparse.ArgumentParser ()
parser.add_argument ('-f', '--folder', help="Folder name in directory--> img", required=True, type=str)
parser.add_argument ("-e", "--ext", help="extension you are renaming to", required=True, type = str)
parser.add_argument ("-e_r1", "--er1", help="first extension you are removing", required=True, type=str)
parser.add_argument ("-e_r2", "--er2", help="second extension you are removing", required=True, type=str)
args = parser.parse_args ()


def rename_to_jpg(img_dir, extension, old_format1, old_format2):
    """"This function renames all file format/extension from old_format1 or old_format2 to extension
    e.g i.png to i.jpg"""
    current = str (pathlib.Path ().resolve ())
    img_dir = str(img_dir)
    path = '{}\{}'.format(current, img_dir)
    os.chdir (path)
    files = os.listdir (path)
    len_ext = len (extension)
    len_ext1 = len (old_format1)
    len_ext2 = len (old_format2)
    for file in (files):
        if file[-len_ext:] !=str(extension):
            try:
                if file[-len_ext1:] == str (old_format1):
                    os.rename (os.path.join (path, file), os.path.join (path, ''.join ([str (file[:-len_ext1]), extension])))
                elif file[-len_ext2:] == str(old_format2):
                    os.rename (os.path.join (path, file), os.path.join (path, ''.join ([str (file[:-len_ext2]), extension])))
            except:
                KeyError


if __name__ == '__main__':
    rename_to_jpg (args.folder, args.ext, args.er1, args.er2)
