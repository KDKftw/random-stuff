##test

from selenium import webdriver


from selenium.common.exceptions import NoSuchElementException

URL_stat = "https://www.eximtours.cz/recko"
URL_stat2 = "file:///C:/Users/KDK/Desktop/Nejlepší rodinná dovolená_ Řecko! _ EXIM TOURSnomapa.html"

def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL_stat2)


    try:
        destinaceAll = driver.find_elements_by_xpath( "//*[@class='fshr-listTable-item']")
        destinaceSingle = driver.find_element_by_xpath("//*[@class='fshr-listTable-item']")
        pocetDestinaci = len(destinaceAll)
        print(pocetDestinaci)
        if destinaceSingle.is_displayed():
            for WebElement in destinaceAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("destinace jsou zobrazeny")

                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("destinace se nezobrazují")



    try:
        dlazdiceFotoSingle = driver.find_element_by_xpath("//*[@class='f_tile-image-content']")
        dlazdiceFotoAll = driver.find_elements_by_xpath("//*[@class='f_tile-image-content']")
        if dlazdiceFotoSingle.is_displayed():
            for WebElement in dlazdiceFotoAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("dlazdice foto jsou zobrazeny")

                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("dlazdice foto se nezobrazují")

    try:
        mapa = driver.find_element_by_xpath("//*[@id='google-map']")
        if mapa.is_displayed():
            print("mapa displaynuta")
            pass

        else:
            print("neco je spatne ")
    except NoSuchElementException:
        print("mapa se nezobrazují")





test()