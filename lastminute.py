##LM test

from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException



URL_lm = "https://www.eximtours.cz/last-minute"
URL_lm2 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevyLM.html"
URL_lm3 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevyLM18.html"
URL_lm4 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevy0LM.html"

def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL_lm4)
    try:
        zajezdyLMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
        zajezdyLMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
        pocetZajezdu = len(zajezdyLMall)
        print(pocetZajezdu)
        if zajezdyLMsingle.is_displayed():
            for WebElement in zajezdyLMall:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("zajezdy jsou zobrazeny")

                    if not pocetZajezdu == 20:
                        print("Zajzedu se zobrazuje pouze " , pocetZajezdu)

                elif pocetZajezdu == 0:
                    print("velky spatny")


                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("zajeztdy se nezobrazují")

    try:
        rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
        driver.execute_script("arguments[0].click();", rozbal)
        time.sleep(1)

    except NoSuchElementException:
        print("kek")


    try:
        rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
        rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
        if rozbalenyZajezd.is_displayed():
            for WebElement in rozbalenyZajezdAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("rozbalene zajezdy jsou zobrazeny")

                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("zajeztdy se nezobrazují")

    time.sleep(50)




test()