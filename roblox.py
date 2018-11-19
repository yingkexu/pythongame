# need to install  pywin32. run: 
# pip install pywin32
import win32api
import win32gui
import win32con
import time

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

while True:
    hWnd = win32gui.FindWindow(None, "Roblox")
    print(hWnd)
    win32gui.SetForegroundWindow(hWnd)
    win32gui.SetActiveWindow(hWnd)
   # lParam = win32api.MAKELONG(500, 500)
    #win32gui.SendMessage(hWnd, win32con.WM_LBUTTONDOWN, 0, lParam)
    #win32gui.SendMessage(hWnd, win32con.WM_LBUTTONUP, 0, lParam)
    click(200,200)
    time.sleep(2)