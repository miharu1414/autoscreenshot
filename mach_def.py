from webbrowser import get
import pyautogui as pag
from time import sleep
import os
from re import X
import ctypes
import time

x1 ,x2, y1, y2 = 0,0,0,0
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
    

def get_sukusyo():
  i = 1
  check = 0
  global path
  path = "sukusyo"
  os.mkdir(path)
  try:
    while not check:
      img = pag.screenshot(region= (x1,y1,x2-x1,y2-y1))
      img.save(path + "/img"+str(i)+".png")
      sleep(10)
      i = i + 1
      if i == 10:
        check = 1
  except KeyboardInterrupt:
    print('\n')

mouse()
get_sukusyo()
