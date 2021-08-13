##homepage test
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

URL_HP = "https://www.eximtours.cz/"
URL2_HP = "file:///C:/Users/KDK/Desktop/EXIM%20TOURS%20-%20dovolen%C3%A1,%20z%C3%A1jezdy,%20last%20minute,%20eurov%C3%ADkendy.html"
URL3_HP = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyNONEJLEPSINABADIKY.html"


def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL_HP)
    try:
        bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
        bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
        if bannerSingle.is_displayed():
            for WebElement in bannerAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("Bannery jsou zobrazeny")
                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("Bannery se nezobrazují")

    time.sleep(5)
    try:
        nejnabidkyLMsingle = driver.find_element_by_xpath("//*[@class='f_tourTable-tour']")
        nejnabidkyLMall = driver.find_elements_by_xpath("//*[@class='f_tourTable-tour']")
        if nejnabidkyLMsingle.is_displayed():
            for WebElement in nejnabidkyLMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("LM - Nabídka je zobrazena")
                else:
                    print("neco je spatne ")


    except NoSuchElementException:
        print("Nejlepsi nabidky LM se neukazuji")


    switchButton = driver.find_element_by_xpath("//*[@class='f_switch-button']")
    driver.execute_script("arguments[0].click();", switchButton)

    time.sleep(4)


    try:
       nejnabidkyFMsingle = driver.find_element_by_xpath("//*[@class='f_tourTable-tour']")
       nejnabidkyFMall = driver.find_elements_by_xpath("//*[@class='f_tourTable-tour']")
       if nejnabidkyFMsingle.is_displayed():

        for WebElement in nejnabidkyFMall:
            jdouvidet = WebElement.is_displayed()
            if jdouvidet == True:
                print("FM - Nabídka je zobrazena")
            else:
                print("neco je spatne ")
    except NoSuchElementException:
     print("Nejlepsi nabidky FM se neukazuji")


    time.sleep(3)

    try:
        topnabidkaSingle = driver.find_element_by_xpath("//*[@class='f_tile-image-content']")
        topnabidkaAll = driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
        if topnabidkaSingle.is_displayed():
            for WebElement in topnabidkaAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                 print("TOP NABIDKA - Nabídka je zobrazena")
                else:
                 print("neco je spatne ")
    except NoSuchElementException:
         print("Top nabídka se nezobrazuje")

    time.sleep(3)













    time.sleep(50)


test()