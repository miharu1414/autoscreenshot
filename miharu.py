# namiki
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox


from re import X
import pyautogui 
import ctypes
import time
import pyautogui as pag
import numpy as np

from itertools import count
import math
from webbrowser import get
import pyautogui as pag
from time import sleep
import time
import os
from re import X
import ctypes
import time
from PIL import Image 
import shutil
import img2pdf
from natsort import natsorted
import imgsim
import cv2


# global 変数

answer_ja = ''





    
    
        #s = input("sと入力してください:")
x1 ,x2, y1, y2 = 0,0,0,0
interval = 2.3
pdf_img = []
doga_m,doga_s,doga_speed = 0,0,0

def tab1_main(tab1):
    bg_col =  '#ffffe0'
    tab1['bg'] = bg_col
    


    def mouse():
        global x1,x2,y1,y2
        print("左上端をクリックしてください")
        messagebox.showinfo('確認', 'スクショ範囲の左上をクリック')
        xy1.delete(0, tk.END)
        xy2.delete(0, tk.END)
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
        messagebox.showinfo('確認', 'スクショ範囲の右下をクリック')
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
    # テキストボックス -> マウスの座標表示      xy.insert(tkinter.END,"1234")で挿入　　　　.get()で取得　.delete(0, tkinter.END)でクリア
        xy1.insert(tk.END,'  ('+str(x1)+','+str(y1)+')')
        xy2.insert(tk.END,'  ('+str(x2)+','+str(y2)+')')
        
            
            

            
            
    def get_sukusyo():
        start = time.perf_counter()
        global pdf_img,interval,a1
        a1 = 0
        pdf_img.clear()
        global doga_m,doga_s,doga_speed
    
        try:
            if doga_m.get() == '':
                minutes = 0
            else:
                minutes = float(doga_m.get())
            print(minutes)
            
            if doga_s.get() == '':
                second = 0
            else:
                second = float(doga_s.get())
            print(second)
            speed = float(doga_speed.get())
            print(doga_speed.get())

            doga_time = (minutes*60 + second)/speed
            print(f'{doga_time}秒スクショします')
            doga_time -= 1.5
        except:
            messagebox.showerror('エラー', '動画時間が適切に入力されていません')
            return 0
            
        
        def judge(path1, path2):
            global a1
            img0 = cv2.imread(path1)
            img1 = cv2.imread(path2)

            vtr = imgsim.Vectorizer()
            vec0 = vtr.vectorize(img0)
            vec1 = vtr.vectorize(img1)
            
            List1 = np.ravel(img0)
            List2 = np.ravel(img1)
            result = np.dot(List1, List2)/(np.linalg.norm(List1)*np.linalg.norm(List2))
            
            
            dist = imgsim.distance(vec0, vec1)
            #dist = np.count_nonzero(img0 == img1) / img1.size
            
            print(result)
            print(a1)
            print(dist)

            

            if a1 !=0:
                if dist/a1 >= 50:
                    a1 = dist
                    return 1

            if dist > 1.5: #if dist < 0.90 and result < 5e-09:
                a1 = dist
                print("yes")
                return 1
            a1 = dist
            print("no")
            return 0
        i = 1
        global path
        path = "sukusyo"
        
        try:
            shutil.rmtree(path)
        except:
            pass
        os.mkdir(path)
        
        abs_path = os. getcwd()
        print(abs_path)
        try:
            start_time = time.perf_counter()
            sleep(3)
            while 1:

                
                
                img = pag.screenshot(region= (x1,y1,x2-x1,y2-y1))
                img.save(path + "/img"+str(i)+".png")
                print( "/img"+str(i)+".png"+"を保存しました")
                if i == 1:
                    pdf_img.append(path+"/img"+str(i)+".png")

                    i = i + 1
                    continue
                if judge(abs_path+'/'+path+"/img"+str(i)+".png",abs_path+'/'+path + "/img"+str(i-1)+".png"):
                    pdf_img.append(abs_path+'/'+path+"/img"+str(i)+".png")
 
                i = i + 1
                timer = time.perf_counter()
                
                end_time = time.perf_counter()
                
                # PC性能の差による処理時間の調整
                if end_time - start_time < interval:
                    sleep(interval - (end_time-start_time))
                if timer-start > doga_time:
                    break
        except KeyboardInterrupt:
            print('\n')
        messagebox.showinfo('確認', 'スライドの撮影が終了しました')
        print(*pdf_img)
        

        return pdf_img

        
        
    def png_to_pdf():
        global pdf_img
        outputpath= "file.pdf"
        try:
            os.remove(outputpath)
        except:
            pass
        layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(257), img2pdf.mm_to_pt(182)))
        pdf_img.pop(0)
        with open(outputpath, "wb") as f:
            f.write(img2pdf.convert([i for i in natsorted(pdf_img) if ".png" in i], layout_fun=layout))
                # フォルダの削除
        messagebox.showinfo('確認', 'PDF化できました')
        shutil.rmtree(path)

            
    # ラベル1の生成
    label1 = tk.Label(tab1, text='1.範囲および時間を指定してください', bg=bg_col,font=("", "13", "bold"))
    label1.pack(padx=5, pady=7)
    
    # ボタンの作成と配置
    label2 = tk.Label(tab1, text='左上：', bg=bg_col)
    label2.place(x=60, y=50, width = 40, height = 32)
    # テキストボックス -> マウスの座標表示      xy.insert(tkinter.END,"1234")で挿入　　　　.get()で取得　.delete(0, tkinter.END)でクリア
    xy1 = tk.Entry(tab1,relief="solid",width=20)
    xy1.place(x=100, y=50, width = 100, height = 32)
    
    label3 = tk.Label(tab1, text='右下：', bg=bg_col)
    label3.place(x=210, y=50, width = 40, height = 32)
    xy2 = tk.Entry(tab1,relief="solid",width=20)
    xy2.place(x=250, y=50, width = 100, height = 32)
    
    mouse_button = tk.Button(tab1, text="範囲決定",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = mouse )
    mouse_button.place(x = 360, y = 50, width = 70, height = 32)
    
    
    height = 26
    label4 = tk.Label(tab1, text='時間：', bg=bg_col)
    label4.place(x=60, y=100, width = 40, height = height)
    
    global doga_s,doga_m,doga_speed

    doga_m = tk.Entry(tab1,relief="solid",width=20, justify="right")
    doga_m.place(x=100, y=100, width = 40, height = height)
    
    label_min = tk.Label(tab1, text='分', bg=bg_col)
    label_min.place(x=140, y=100, width = 20, height = height)
    
    doga_s = tk.Entry(tab1,relief="solid",width=20, justify="right")
    doga_s.place(x=170, y=100, width = 40, height = height)
    
    label_sec = tk.Label(tab1, text='秒', bg=bg_col)
    label_sec.place(x=210, y=100, width = 20, height =  height)
    
    doga_speed = tk.Entry(tab1,relief="solid",width=20, justify="right")
    doga_speed.insert(0, "1")
    doga_speed.place(x=240, y=100, width = 40, height = height)
    
    label_sec = tk.Label(tab1, text='倍', bg=bg_col, fg = "#707070")
    label_sec.place(x=280, y=100, width = 20, height = height)
    


    # スクショのスタート
    label6 = tk.Label(tab1, text='2.スタートボタンを押してください', bg=bg_col,font=("", "13", "bold"))
    label6.place(x=43, y=140, width =380, height = 32)
    
    
    start_button = tk.Button(tab1, text="スタート",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = get_sukusyo)
    start_button.place(x = 160, y = 190, width = 120, height = 60)
    
    # スクショのスタート
    label7 = tk.Label(tab1, text='3.PDFに出力します', bg=bg_col,font=("", "13", "bold"))
    label7.place(x=50, y=260, width =200, height = 32)
    
    
    start_button = tk.Button(tab1, text="出力",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = png_to_pdf)
    start_button.place(x = 160, y = 320, width = 120, height = 60)
    
    
    
    
    
    return 0