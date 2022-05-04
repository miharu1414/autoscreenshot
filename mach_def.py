from webbrowser import get
import pyautogui as pag
from time import sleep
import os
from re import X
import ctypes
import time
from PIL import Image 
import imagehash 
import shutil

x1 ,x2, y1, y2 = 0,0,0,0
interval = 5

def mouse():
    global x1,x2,y1,y2
    print("左上端をクリックしてください")
    try:
        while True:
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                x, y = pag.position()
                print(str(x) + ':' + str(y))
                x1 = x
                y1 = y
                time.sleep(1)
                break
            ### ここにクリック時の動作を記入する ###

    except KeyboardInterrupt:
        print('左上端終了')
    
    
    print("右下端をクリックしてください")
    try:
        while True:
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                x, y = pag.position()
                print(str(x) + ':' + str(y))
                x2 = x
                y2 = y
                break
            ### ここにクリック時の動作を記入する ###

    except KeyboardInterrupt:
        print('右下端終了')
        #s = input("sと入力してください:")
    

def get_sukusyo(pdf_img,interval):
    def judge(path1,path2) -> bool:
        hash = imagehash.average_hash(Image.open(path1)) 
        print(hash) 
        
        otherhash = imagehash.average_hash(Image.open(path2)) 
        print(otherhash) 
        
        print(hash == otherhash) 
        print(hash - otherhash)
        return hash == otherhash
    i = 1
    check = 0
    global path
    path = "sukusyo"
    os.mkdir(path)
    try:
        while 1:
            img = pag.screenshot(region= (x1,y1,x2-x1,y2-y1))
            img.save(path + "/img"+str(i)+".png")
            print( "/img"+str(i)+".png"+"を保存しました")
            if i == 1:
                pdf_img.append(path+"/img"+str(i)+".png")
                sleep(interval)
                i = i + 1
                continue
            if not judge(path+"/img"+str(i)+".png",path + "/img"+str(i-1)+".png"):
                pdf_img.append(path+"/img"+str(i)+".png")
            sleep(interval)
            i = i + 1
            if i == 10:
                break
    except KeyboardInterrupt:
        print('\n')
    
    return pdf_img
    
    




mouse()
pdf_img =[]

get_sukusyo(pdf_img, interval)
print(pdf_img)

shutil.rmtree(path)