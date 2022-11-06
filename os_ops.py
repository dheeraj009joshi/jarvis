import os
import subprocess as sp
import pyautogui


paths = {
   
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])


def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])
    
    
def screenShot(filename):
    try:
        os.mkdir("output_screenshot")
    except:
        pass
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'output_screenshot/{filename}.png')