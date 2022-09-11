##just a quick script that was helping me to autosave my favorite game as I was used to

import pyautogui
import time
import keyboard



def quicksave():
    while True:

        if keyboard.read_key() == "f5":
            ##keyboard.Key("p"):
            pyautogui.press("ESC")
            time.sleep(0.2)
            pyautogui.press("ENTER")
            time.sleep(0.1)
            pyautogui.press("ENTER")
            time.sleep(0.1)
            pyautogui.press("ENTER")
        else:
            time.sleep(0.1)




def cook():
    if keyboard.read_key() == "f9":
            quit()


    if keyboard.read_key() == "f8":
        cook2()


def cook2():
    x= 0
    while x < 17:
        pyautogui.click()
        time.sleep(1.2)
        x=x+1
        print(x)


quicksave()




