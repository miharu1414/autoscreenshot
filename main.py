from itertools import count
from math import dist
from webbrowser import get
from numpy import double
import pyautogui as pag
from time import sleep
import time
import os
from re import X
import ctypes
import time
from PIL import Image 
import imagehash 
import shutil
import img2pdf
from natsort import natsorted
import imgsim
import cv2

x1 ,x2, y1, y2 = 0,0,0,0
interval = 0.1
start = time.perf_counter()
print("動画時間を入力してください:", end="")
doga = double(input())

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
	def judge(path1, path2, a1):
		img0 = cv2.imread(path1)
		img1 = cv2.imread(path2)

		vtr = imgsim.Vectorizer()
		vec0 = vtr.vectorize(img0)
		vec1 = vtr.vectorize(img1)

		dist = imgsim.distance(vec0, vec1)
		print(dist)

		if a1 !=0:
			if dist/a1 >= 5:
				a1 = dist
				return 1
		elif dist > 1:
			a1 = dist
			return 1
		a1 = dist
		return 0
	i = 1
	global path
	path = "sukusyo"
	os.mkdir(path)
	try:
		global a1
		a1 = 0
		while 1:
			img = pag.screenshot(region= (x1,y1,x2-x1,y2-y1))
			img.save(path + "/img"+str(i)+".png")
			print( "/img"+str(i)+".png"+"を保存しました")
			if i == 1:
				pdf_img.append(path+"/img"+str(i)+".png")
				sleep(interval)
				i = i + 1
				continue
			if judge(path+"/img"+str(i)+".png",path + "/img"+str(i-1)+".png", a1):
				pdf_img.append(path+"/img"+str(i)+".png")
			sleep(interval)
			i = i + 1
			timer = time.perf_counter()
			if timer-start > doga:
				break
	except KeyboardInterrupt:
		print('\n')
	
	return pdf_img


def png_to_pdf(a):
	outputpath= "file.pdf"
	layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(257), img2pdf.mm_to_pt(182)))
	with open(outputpath, "wb") as f:
		f.write(img2pdf.convert([i for i in natsorted(a) if ".png" in i], layout_fun=layout))


mouse()
pdf_img =[]

get_sukusyo(pdf_img, interval)
print(pdf_img)
png_to_pdf(pdf_img)

shutil.rmtree(path)

