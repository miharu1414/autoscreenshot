#タブを3つ持つGUIウィンドウを作成する。

#import
import tkinter as tk
import tkinter.ttk as ttk

from miharu import tab1_main
from hiroki import tab2_main
from sonota import tab3_main

def main():

    #メインウィンドウ作成
    main_view = tk.Tk()

    #メインウィンドウのタイトルを変更
    main_view.title("大学生活のアプリ")

    #メインウィンドウの大きさを設定
    main_view.geometry("500x450")

    #メインウィンドウにnotebookを作成する。
    nb = ttk.Notebook(main_view)

    #notebookに関するフレームを3つ作る。
    tab1 = tk.Frame(nb)
    tab2 = tk.Frame(nb)
    tab3 = tk.Frame(nb)

    #notebookに対してtab1, 2, 3をそれぞれ追加する。
    nb.add(tab1, text="tab1", padding=3)
    nb.add(tab2, text="tab2", padding=3)
    nb.add(tab3, text="tab3", padding=3)

    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")

    #各タブの内容を記載する。
    tab1_main(tab1)
    tab2_main(tab2)
    tab3_main(tab3)

    #main_viewを表示する無限ループ
    main_view.mainloop()

    return 0




if __name__ == "__main__":
    main()