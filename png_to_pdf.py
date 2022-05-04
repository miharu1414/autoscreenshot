import pyautogui as pag
from time import sleep
import os
import img2pdf
from natsort import natsorted
from PIL import Image


def png_to_pdf(a):
  outputpath= "file.pdf"
  layout = img2pdf.get_layout_fun((img2pdf.mm_to_pt(257), img2pdf.mm_to_pt(182)))
  with open(outputpath, "wb") as f:
    f.write(img2pdf.convert([str(i) for i in natsorted(a) if ".png" in i], layout_fun=layout))

a = {"img1.png", "img2.png", "img3.png"}

png_to_pdf(a)


