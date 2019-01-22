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

# content of picture folder
picturelist = os.listdir(file_path)
index = 0

def checkpic():
    global index
    # create viewer windows, resize picture
    img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
    h, w, r = 0, 0, 0
    h, w, r = img.shape
    if (h < 301) and (w < 301):
        shutil.move(str(file_path)+"/"+str(picturelist[index]), str(todelete)+"/"+str(picturelist[index]))
        del picturelist[index]
        index += 1
        viewpic()

def viewpic():
    global index
    checkpic()
    # create viewer windows, resize picture
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    img = cv2.imread(filename = str(file_path)+"/"+str(picturelist[index]))
    h, w, r = 0, 0, 0
    h, w, r = img.shape
    ratio = w / h
    height = 800
    width = int(height * ratio)
    cv2.resizeWindow('image',(width, height))
    cv2.imshow('image',img)

def picloop():
    global index
    while(1):
        k = cv2.waitKeyEx(0)
        if k==27:           # wait for ESC key to exit
            cv2.destroyAllWindows()
            break
        elif k==2490368:    # cursor up move to delete folder
            shutil.move(str(file_path)+"/"+str(picturelist[index]), str(todelete)+"/"+str(picturelist[index]))
            del picturelist[index]
            viewpic()
        elif k==2621440:    #cursor down move to sort folder
            shutil.move(str(file_path)+"/"+str(picturelist[index]), str(sort)+"/"+str(picturelist[index]))
            del picturelist[index]
            viewpic()
        elif k==2424832:    # cursor left previous picture
            print(index)
            index -= 1
            if index < 0:
                index = 0
            print("vor view")
            print(index)
            viewpic()
        elif k==2555904:    # cursor right next picture
            index += 1
            if index > len(picturelist)-1:
                index = len(picturelist)-1
            viewpic()
        elif k==-1:         # ignore waitkey standard input
            continue
        else:               # print every other pressed key
            print(k)    

if __name__ == '__main__':
    viewpic()
    picloop()
