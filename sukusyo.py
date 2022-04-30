import pyautogui as pag
from time import sleep
import os

def get_sukusyo():
  i = 1
  savepath = 'C:/Users/iga3s/Documents'
  global path
  path = os.getcwd() + "/sukusyo"
  os.mkdir(path)

  check = 0
  try:
      while not check:
          img = pag.screenshot(path + '/screenshot' + str(i) + '.png')
          sleep(10)
          i = i + 1
          if i == 10:
            check = 1
  except KeyboardInterrupt:
      print('\n')

get_sukusyo()

