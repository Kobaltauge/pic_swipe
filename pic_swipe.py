import tkinter as tk
from tkinter import filedialog
import os
import cv2
import sys
import shutil

# output folder
sort = "e:/pic_swipe/sort/"
todelete = "e:/pic_swipe/delete/"

# File dialog for picing picture folder
root = tk.Tk()
root.withdraw()
file_path = os.path.dirname(filedialog.askopenfilename())

# content of picutre folder
picturelist = os.listdir(file_path)
index = 0

# create viewer windows, resize picture
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
cv2.resizeWindow('image',800, 600)
cv2.imshow('image',img)

while(1):
    k = cv2.waitKeyEx(0)
    if k==27:           # wait for ESC key to exit
        cv2.destroyAllWindows()
        break
    elif k==2490368:    # cursor up move to delete folder
        shutil.move(str(file_path)+"/"+str(picturelist[index]), str(todelete)+"/"+str(picturelist[index]))
        index += 1
        img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
        cv2.resizeWindow('image',800, 600)
        cv2.imshow('image',img)
    elif k==2621440:    #cursor down move to sort folder
        shutil.move(str(file_path)+"/"+str(picturelist[index]), str(sort)+"/"+str(picturelist[index]))
        index += 1
        img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
        cv2.resizeWindow('image',800, 600)
        cv2.imshow('image',img)
    elif k==2424832:    # cursor left previous picture
        index -= 1
        if index < 0:
            index = 0
        img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
        cv2.resizeWindow('image',800, 600)
        cv2.imshow('image',img)
    elif k==2555904:    # cursor right next picture
        index += 1
        img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
        cv2.resizeWindow('image',800, 600)
        cv2.imshow('image',img)
    elif k==-1:         # ignore waitkey standard input
        continue
    else:               # print every other pressed key
        print(k)    
