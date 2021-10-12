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


hWnd = win32gui.FindWindow(None, "无标题 - 画图")
print(hWnd)
win32gui.SetForegroundWindow(hWnd)
win32gui.SetActiveWindow(hWnd)
win32api.SetCursorPos((300,300))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,300,300,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,800,400,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,800,400,0,0)