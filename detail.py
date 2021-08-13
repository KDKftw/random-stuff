##detail of a hotel testing script

from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException

URL = "https://www.eximtours.cz/egypt/hurghada/hurghada/hotel-bella-vista"
URL2 = "file:///C:/Users/KDK/Desktop/BELLA VISTA _ EXIM TOURSnofoto.html"
URL3 = "file:///C:/Users/KDK/Desktop/OA BELORIZONTE _ EXIM TOURSnoterminy.html"


def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL3)
    try:
        detailFotka = driver.find_element_by_xpath("//*[@class='fshr-detailGallery']")
        if detailFotka.is_displayed():
            pass
            print("fotka ok")
    except NoSuchElementException:
        print("fotka se nezobrazují")

    try:
        sedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
        if sedivka.is_displayed():
            pass
            print("sedivka ok")

    except NoSuchElementException:
        print("fotka se nezobrazují")

    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='terminyaceny-tab']").click()
    time.sleep(1)
    potvrdit2 = driver.find_element_by_xpath("//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-popupWindow--close']")
    driver.execute_script("arguments[0].click();", potvrdit2)
    time.sleep(1)
    try:
        terminyAll = driver.find_elements_by_xpath(
            "//*[@class='js-sorting-item fshr-termins-table-item js-detailFilter tour-row js-priceUpdated']")
        terminySingle = driver.find_element_by_xpath(
            "//*[@class='js-sorting-item fshr-termins-table-item js-detailFilter tour-row js-priceUpdated']")
        pocetTerminu = len(terminyAll)
        print(pocetTerminu)
        if terminySingle.is_displayed():
            for WebElement in terminyAll:
                jdouvidet = WebElement.is_displayed()
                if jdouvidet == True:
                    print("¨terminy jsou zobrazeny")


                elif pocetTerminu == 0:
                    print("velky spatny")


                else:
                    print("neco je spatne ")
    except NoSuchElementException:
        print("terminy se nezobrazují")


    time.sleep(50)

test()