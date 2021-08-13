##trying to detect a image on my screen to play the loop

import pyautogui
import time
def proRoper2():
    while True:
        time.sleep(3)
        if (pyautogui.locateOnScreen(r"C:\Users\KDK\Desktop\HS klikacka\odd.png")) is not None:
            time.sleep(3)
            pyautogui.click(1368, 854)      ##play button deck select
            print("play")
            time.sleep(81)
            time.sleep(89)
            pyautogui.click(1127, 789)
            time.sleep(1)
            pyautogui.click(1127, 789)
            time.sleep(1)
            pyautogui.click(1127, 789)
            time.sleep(1.5)
            pyautogui.click(1127, 789)
            time.sleep(1.5)
            pyautogui.click(1127, 789)
            time.sleep(1)
            pyautogui.click(1127, 789)
            time.sleep(1)
            pyautogui.click(1127, 789)
            time.sleep(1.5)
            pyautogui.click(1127, 789)
            time.sleep(1.5)

        else:

            time.sleep(0.5)


proRoper2()