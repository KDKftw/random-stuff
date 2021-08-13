from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

URL_search = "https://www.eximtours.cz/vysledky-vyhledavani?tt=0&ac1=2&kc1=1&ka1=6&ic1=0&ht=77&dd=2021-07-01&rd=2021-08-31&er=0&nn=7|8|9&d=63220|63316|63319|63324|63333|63402|63390|63409|63471&pf=0&pt=900000"
URL_search2 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyHOTELY.html"
URL_search3 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyFOTKARIP.html"
URL_search4 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyFOTKYRIP19.html"
URL_search5 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyCENY19v2.html"

def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL_search)
    try:
        hotelySingle = driver.find_element_by_xpath("//*[@id='divHotelCard']")
        hotelyAll = driver.find_elements_by_xpath("//*[@id='divHotelCard']")
        pocetHotelu = len(hotelyAll)
        if hotelySingle.is_displayed():
            for WebElement in hotelyAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("Hotely jsou zobrazeny")

                    if not pocetHotelu == 20:
                        print("Hotelu se zobrazuje pouze " , pocetHotelu)
                else:
                    print("neco je spatne")
    except NoSuchElementException:
        print("Hotely se nezobrazují")


    try:
        fotkyAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
        fotkaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
        pocetFotek = len(fotkyAll)
        print(pocetFotek)
        if fotkaSingle.is_displayed():
            for WebElement in fotkyAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("Fotky hotelu jsou zobrazeny")

                    if not pocetFotek == 20:
                        print("Fotek Hotelu se zobrazuje pouze " , pocetHotelu)
                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("FOtky hotelu se nezobrazují")




    try:
        cenaAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResult-item-summary']")
        cenaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResult-item-summary']")
        pocetCen = len(cenaAll)
        print(pocetCen)
        if cenaSingle.is_displayed():
            for WebElement in cenaAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("Ceny hotelu jsou zobrazeny")

                    if not pocetCen == 20:
                        print("Ceny Hotelu se zobrazuje pouze ", pocetCen)
                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("ceny hotelu se nezobrazují")










test()