##simply click and return to previous postion

import pyautogui
import time


def fuckyoublizz():
    while True:
        pyautogui.size()


        time.sleep(60)
        #pyautogui.click(2642,864)
        pyautogui.click(2780, 854)
        ##time.sleep(5)
        ##pyautogui.click(2780, 854)
        ##time.sleep(5)
        ##pyautogui.click(2780, 854)
        

def fuckyoublizz2():
    while True:
        time.sleep(60)
        pozice =  pyautogui.position()
        print(pozice)
        pyautogui.moveTo(2780, 854)
        pyautogui.click(2780, 854)
        #time.sleep(0.5)
        pyautogui.moveTo(pozice)

fuckyoublizz2()