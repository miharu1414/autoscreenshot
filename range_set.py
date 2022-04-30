from re import X
import pyautogui 
import ctypes
import time

x1 ,x2, y1, y2 = 0,0,0,0
def mouse():
    global x1,x2,y1,y2
    print("左上端をクリックしてください")
    try:
        while True:
            if ctypes.windll.user32.GetAsyncKeyState(0x01) == 0x8000:
                x, y = pyautogui.position()
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
                x, y = pyautogui.position()
                print(str(x) + ':' + str(y))
                x2 = x
                y2 = y
                break
            ### ここにクリック時の動作を記入する ###

    except KeyboardInterrupt:
        print('右下端終了')
    while 1:
        #s = input("sと入力してください:")
        if 1:
            screen_shot = pyautogui.screenshot(region = (x1,y1,x2-x1,y2-y1)) 
            screen_shot.save('test.png')
            break
        else:
            print("正常に入力されていません．")
mouse()