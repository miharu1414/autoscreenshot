# namiki
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from googletrans import Translator

from re import X
import pyautogui 
import ctypes
import time
import pyautogui as pag
# global 変数
answer_ja = ''





    
    
        #s = input("sと入力してください:")
x1 ,x2, y1, y2 = 0,0,0,0

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
    
    label4 = tk.Label(tab1, text='時間：', bg=bg_col)
    label4.place(x=60, y=100, width = 40, height = 32)
    
    doga = tk.Entry(tab1,relief="solid",width=20)
    doga.place(x=100, y=100, width = 100, height = 32)
    
    label5 = tk.Label(tab1, text='※2倍再生の場合は÷2した時間', bg=bg_col, fg = "#707070")
    label5.place(x=220, y=100, width = 200, height = 32)


    # スクショのスタート
    label5 = tk.Label(tab1, text='2.スタートボタンを押してください', bg=bg_col,font=("", "13", "bold"))
    label5.place(x=45, y=140, width =400, height = 32)
    
    
    start_button = tk.Button(tab1, text="スタート",relief="solid", bg="white", fg = "#2f4f4f",bd=1, command = mouse )
    start_button.place(x = 160, y = 190, width = 120, height = 60)
    

    
    
    
    
    return 0

