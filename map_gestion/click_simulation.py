import win32con as wcon
import win32gui
import win32api

import time

class ClickSimulation():
    
    
    def __init__(self):
        
        self.hwnd = win32gui.FindWindow(None, "Dofus Retro") 
        self.base_size_X = 14
        self.base_size_Y = 32
        
    def click(self,cell):
        rect = win32gui.GetWindowRect(self.hwnd)
        
        
        x = (cell["x"])*2-2
        y = cell["y"] -2

        
        if x%2 == 0:
            scallX = (self.base_size_X+1)/cell["max_x"]
        else:
            scallX = self.base_size_X/cell["max_x"]

            
        scallY = self.base_size_Y/cell["max_y"]
        
        print(scallX,scallY)
        if y%2 != 0:
            x = 24+26*x       
            y = 28+13.5*y
        else:
            x = 51+24.55*x
            y = 28+13.5*y
            
        x = round(x * scallX)
        y = round(y * scallY)

        #la premiere valeur represente l'ecart de la cell en fonction de la base de la carte
        #la valeur miltiplier represente l'ecart entre charque case
        lParam = win32api.MAKELONG(x, y)
        win32gui.PostMessage(self.hwnd, wcon.WM_MOUSEMOVE, 0x01, lParam)



        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONUP,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONUP,wcon.MK_LBUTTON, lParam)
    
        #win32gui.PostMessage(self.hwnd, wcon.WM_RBUTTONDOWN,wcon.MK_RBUTTON, lParam)



if __name__ == "__main__":
    x = ClickSimulation()

    x.click(18,39)

    time.sleep(0.2)