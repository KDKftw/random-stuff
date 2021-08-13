##every 60secs click armorup

 ## 1:19 cca do druheho kola
  ## 1:11     ##lognuto do hry az dokonce confir a start hry

import pyautogui
import time

def test():
    while True:
        time.sleep(3)
        if (pyautogui.locateOnScreen(r"C:\Users\KDK\Desktop\HS klikacka\mycollection.png")) is not None:
            x=0
            pyautogui.click(1368, 854)
            time.sleep(81)
            time.sleep(89)
            while x > 15:
                pyautogui.click(1127, 789)
                time.sleep(1)
                x=x+1

        else:
            time.sleep(60)
            pyautogui.click(1127, 789)


test()