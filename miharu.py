# namiki
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from googletrans import Translator
 
# global 変数
answer_ja = ''



def tab1_main(tab1):
    
   
 
    tr = Translator()
    result = tr.translate("hello", src="en", dest="ja").text
    print(result)
    bg_col =  '#ffffe0'
    tab1['bg'] = bg_col


    #文字を表示する。
    param_name = tk.Label(tab1, text="Tlanslater",font=('',18),bg = bg_col)
    param_name.place(x=10, y=10)
    
    # テキストボックス
    text_box = tk.Text(tab1, width = 65, bg="#e0ffff", fg="#2f4f4f", insertbackground="#2f4f4f",
                relief="ridge", bd=5,height=10)
    
    text_box.place(x= 10, y= 40)

    ok_button = tk.Button(tab1, text="OK", width = 7, relief="solid", bd=1)
    ok_button.place(x=220,y = 190)

    # テキストの入力完了ボタン
    def ok_click():
        global answer_ja
        input_text = text_box.get("1.0", "end")
        print(input_text)
        answer_ja = input_text
        click_export_button()
    ok_button["command"] = ok_click


    # 出力処理
    def click_export_button():
        # 翻訳
        tr = Translator()
        result = tr.translate(answer_ja, src="ja", dest="en").text
        print(f'翻訳前 :{result}')
        
        # 
        
        textBox.delete("1.0","end")
        
        textBox.insert(END, result)
        


    # テキスト出力ボックスの作成

    #文字を表示する。
    param_name = tk.Label(tab1, text="出力",font=('',11), bg =  bg_col)
    param_name.place(x=10, y=218)
    textBox = Text(tab1, width=67,height=10)
    textBox.place(x=10,y = 240)


    return 0

