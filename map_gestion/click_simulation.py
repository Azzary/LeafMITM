import win32con as wcon
import win32gui
import win32api
import threading
import time
from copy import  copy
class ClickSimulation():
    
    
    def __init__(self):
        
        self.hwnd = win32gui.FindWindow(None, "Dofus Retro") 
        self.base_size_X = 14
        self.base_size_Y = 32
    
    def test(self):
        win32gui.PostMessage(self.hwnd, wcon.WM_KEYDOWN, wcon.VK_SHIFT, 85464)
        for i in range(10):
            win32gui.PostMessage(self.hwnd, wcon.WM_KEYDOWN, wcon.VK_SHIFT, 8888)
            time.sleep(0.07)
        win32gui.PostMessage(self.hwnd, wcon.WM_KEYUP, wcon.VK_SHIFT, 8888)
        #threading.Thread(None,self.test).start()
        lParam = self.found_lParam(cell)
        time.sleep(0.3)
        win32gui.ShowWindow(self.hwnd,5)
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.PostMessage(self.hwnd, wcon.WM_ACTIVATE, 0, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_MOUSEMOVE, 0, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN, wcon.MK_LBUTTON|wcon.MK_SHIFT, lParam)
        #win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN, wcon.MK_LBUTTON|wcon.MK_SHIFT, lParam)

        time.sleep(0.15)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONUP,wcon.MK_SHIFT, lParam)
        
    def shift_click(self, cell):
        lParam = self.found_lParam(cell)
        self.click(cell)
        
        celltemp = copy(cell)
        
        celltemp["x"] += 1.2
        celltemp["y"] += 2
        time.sleep(0.3)
        self.click(celltemp)
        
        
        
    def found_lParam(self,cell,x_to_add = 0):
        rect = win32gui.GetWindowRect(self.hwnd)
        x = (cell["x"])*2-2
        y = cell["y"] -2

        
        if x%2 == 0:
            scallX = (self.base_size_X+1)/cell["max_x"]
        else:
            scallX = self.base_size_X/cell["max_x"]
        scallY = self.base_size_Y/cell["max_y"]
        
        x += x_to_add*2
        
        if y%2 != 0:
            x = 24+26.7*x       
            y = 28+13.5*y
        else:
            x = 51+24.55*x
            y = 28+13.5*y
            
        x = round(x * scallX)
        y = round(y * scallY)
        
        lParam = win32api.MAKELONG(x, y)
        return lParam
    
    def click(self,cell):
        lParam = self.found_lParam(cell)
        
        win32gui.PostMessage(self.hwnd, wcon.WM_MOUSEMOVE, 0, lParam)
        
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONUP,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONDOWN,wcon.MK_LBUTTON, lParam)
        win32gui.PostMessage(self.hwnd, wcon.WM_LBUTTONUP,wcon.MK_LBUTTON, lParam)
    
        #win32gui.PostMessage(self.hwnd, wcon.WM_RBUTTONDOWN,wcon.MK_RBUTTON, lParam)



if __name__ == "__main__":
    x = ClickSimulation()

    x.click(18,39)

    time.sleep(0.2)