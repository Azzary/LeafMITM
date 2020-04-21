import  pywin32_system32
import win32con as wcon

import win32gui

import win32api
from math import *
from window import Window
import time
import platform
import ctypes



def test(x,y):
    hwnd = win32gui.FindWindow(None, "Dofus Retro") 

    rect = win32gui.GetWindowRect(hwnd)
    
    x = (x*2)-1
    y = y -1
    
    if y%2 == 0:
        y-=1
    
    #For cellID odd 
    if x %2 != 0:
        x = 24+26.7*x  #53*x
        y = 14+13.5*y
    else:
        x = 51+26.7*(x-1)  #+53*x
        y = 28+13.5*y

    x = int(x)
    y = int(y)
    
    #la premiere valeur represente l'ecart de la cell en fonction de la base de la carte
    #la valeur miltiplier represente l'ecart entre charque case
    
    lParam = win32api.MAKELONG(x, y)
    print(lParam)
    win32gui.PostMessage(hwnd, wcon.WM_MOUSEMOVE, 0x01, lParam)


    

    button = ""



    if button == "":
                
        win32gui.PostMessage(hwnd, wcon.WM_LBUTTONDOWN,
                                wcon.MK_LBUTTON, lParam)
    
        win32gui.PostMessage(hwnd, wcon.WM_LBUTTONUP,
                                wcon.MK_LBUTTON, lParam)
    else:
        win32gui.PostMessage(hwnd, wcon.WM_RBUTTONDOWN,
                                wcon.MK_RBUTTON, lParam)
        
        


for i in range(20):
    if i%2 == 0:
        test(6,28)
    else:
        test(6,24)
    time.sleep(2)