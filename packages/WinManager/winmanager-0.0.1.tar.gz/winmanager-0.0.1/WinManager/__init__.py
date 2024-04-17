import win32gui
from win32con import SW_SHOWNORMAL, SW_HIDE
import psutil
from os import system

def windowHandler(hwnd, windows:list):
        windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def getsize(window_title:str):
    """Get the window's size:
        `window_title`: the title of the window you chose (E.G: Windows Powershell)"""
    windows = []
    win32gui.EnumWindows(windowHandler, windows)
    for hwnd, title in windows:
        if window_title.lower() in title.lower():
            size = list(win32gui.GetWindowRect(hwnd))
            return size[2], size[3]
    raise SyntaxError(f"Couldn't find {window_title}!")

def ontop(window_title:str, hide=False):
    """Sets a window on top of the screen:
        `window_title`: the title of the window you chose (E.G: Windows Powershell)
    returns:
        `True` if window found, 'False' if window not found
        """
    
    windows = []
    win32gui.EnumWindows(windowHandler, windows)
    for hwnd, title in windows:
        if window_title.lower() in title.lower():
            win32gui.ShowWindow(hwnd, SW_SHOWNORMAL) if not hide else win32gui.ShowWindow(hwnd, SW_HIDE)
            return True
    return False

def close(AppName:str):
    """Terminates a program:
        `Appname`: the process name (E.G: Notepad++.exe)
    returns:
        `True` if process found, 'False' if not found"""
    if AppName in (i.name() for i in psutil.process_iter()):
        system(f"TASKKILL /F /IM {AppName}")
        return True
    raise SyntaxError(f"Couldn't find {AppName}")

def reposition(window_title:str, y:int, x:int, width:int=-1, height:int=-1):
    """Move and resize a window
        `width` and `height` stay the same if they stay `-1`"""
    width = getsize(window_title)[0] if width == -1 else width
    height = getsize(window_title)[1] if height == -1 else height
    
    windows = []
    win32gui.EnumWindows(windowHandler, windows)
    for hwnd, title in windows:
        if window_title.lower() in title.lower():
            win32gui.MoveWindow(hwnd, x, y, width, height, False)
            return True
    return False

def open(path:str):
    """Open a program by path (E.G: "`C:/Program Files/Notepad++/notepad++.exe`")"""
    path = path.replace('\\', '/')
    system(f'"{path}"')

def getPID(process_name:str):
    """Get PID from process name (E.G: `notepad++.exe`)"""
    for process in psutil.process_iter():
        try:
            if process.name() == process_name:
                return process.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    raise SyntaxError(f"Couln't find {process_name}!")
