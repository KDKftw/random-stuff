##first version of test set, beware that is not a clean code
##multiple URL locations, html files which had which had common problems that accured on the website - to test if Im gonna detect them
import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.eximtours.cz"
URL2 = "file:///C:/Users/KDK/Desktop/BELLA VISTA _ EXIM TOURSnofoto.html"
URL3 = "file:///C:/Users/KDK/Desktop/OA BELORIZONTE _ EXIM TOURSnoterminy.html"
URL_search = "https://www.eximtours.cz/vysledky-vyhledavani?tt=0&ac1=2&kc1=1&ka1=6&ic1=0&ht=77&dd=2021-07-01&rd=2021-08-31&er=0&nn=7|8|9&d=63220|63316|63319|63324|63333|63402|63390|63409|63471&pf=0&pt=900000"
URL_search2 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyHOTELY.html"
URL_search3 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyFOTKARIP.html"
URL_search4 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyFOTKYRIP19.html"
URL_search5 = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyCENY19v2.html"
URL_HP = "https://www.eximtours.cz/"
URL2_HP = "file:///C:/Users/KDK/Desktop/EXIM%20TOURS%20-%20dovolen%C3%A1,%20z%C3%A1jezdy,%20last%20minute,%20eurov%C3%ADkendy.html"
URL3_HP = "file:///C:/Users/KDK/Desktop/EXIM TOURS - dovolená, zájezdy, last minute, eurovíkendyNONEJLEPSINABADIKY.html"
URL_lm = "https://www.eximtours.cz/last-minute"
URL_lm2 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevyLM.html"
URL_lm3 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevyLM18.html"
URL_lm4 = "file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevy0LM.html"
URL_FM = "https://www.eximtours.cz/first-minute"
URL_stat = "https://www.eximtours.cz/recko"
URL_stat2 = "file:///C:/Users/KDK/Desktop/Nejlepší rodinná dovolená_ Řecko! _ EXIM TOURSnomapa.html"
URL_stat = "https://www.eximtours.cz/recko"
URL_stat2 = "file:///C:/Users/KDK/Desktop/Nejlepší rodinná dovolená_ Řecko! _ EXIM TOURSnomapa.html"

driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
wait = WebDriverWait(driver, 25)

class TEST(unittest.TestCase):

    def test_SearchDetail(self):
        driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
        driver.get(URL)
        try:
            lmZajezdNej = driver.find_element_by_xpath("//*[@class='f_tourTable-tour-item f_tourTable-tour-item--destination']")
            wait.until(EC.visibility_of(lmZajezdNej))
            lmZajezdNej.click()


        except:
            print("nenasel lmzajezdnej")
            self.fail()


        try:
            hotelySingle = driver.find_element_by_xpath("//*[@id='divHotelCard']")
            hotelyAll = driver.find_elements_by_xpath("//*[@id='divHotelCard']")
            wait.until(EC.visibility_of(hotelySingle))
            if hotelySingle.is_displayed():
                for WebElement in hotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        print("Hotely jsou zobrazeny")
                    else:
                        print("neco je spatne")
                        self.fail()
        except NoSuchElementException:
            print("Hotely se nezobrazují")
            self.fail()

        try:
            fotkyAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
            fotkaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResults-thumbnail']")
            wait.until(EC.visibility_of(fotkaSingle))
            if fotkaSingle.is_displayed():
                for WebElement in fotkyAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        print("Fotky hotelu jsou zobrazeny")
                    else:
                        print("neco je spatne ")
                        self.fail()
        except NoSuchElementException:
            print("FOtky hotelu se nezobrazují")
            self.fail()

        try:
            cenaAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResult-item-summary']")
            cenaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResult-item-summary']")
            wait.until(EC.visibility_of(cenaSingle))
            if cenaSingle.is_displayed():
                for WebElement in cenaAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        print("Ceny hotelu jsou zobrazeny")
                    else:
                        print("neco je spatne ")
                        self.fail()

        except NoSuchElementException:
            print("ceny hotelu se nezobrazují")
            self.fail()

        try:
            detailHotelu = driver.find_element_by_xpath("//*[@class='fshr-bubble-wrapper']")
            wait.until(EC.visibility_of(detailHotelu))
            detailHotelu.click()


        except NoSuchElementException:
            self.fail()

        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])


        try:
            detailFotka = driver.find_element_by_xpath("//*[@class='fshr-detailGallery']")
            wait.until(EC.visibility_of(detailFotka))
            if detailFotka.is_displayed():
                pass
                print("fotka ok")
        except NoSuchElementException:
            print("fotka se nezobrazují")
            self.fail()

        try:
            sedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
            wait.until(EC.visibility_of(sedivka))
            if sedivka.is_displayed():
                pass
                print("sedivka ok")

        except NoSuchElementException:
            print("fotka se nezobrazují")
            self.fail()
        try:
            terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            terminyCeny.click()
            potvrdit = driver.find_element_by_xpath("//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-popupWindow--close']")
            driver.execute_script("arguments[0].click();", potvrdit)
        except NoSuchElementException:
            print("nenalezeny termíny a ceny")

        try:
            terminySingle = driver.find_element_by_xpath("//*[@data-hotel]")
            wait.until(EC.visibility_of(terminySingle))

            if terminySingle.is_displayed():
                pass
            else:
                 print("neco je spatne ")
                 self.fail()

        except NoSuchElementException:
            print("terminy se nezobrazují")
            self.fail()

        driver.quit()

    def test_HomePage(self):
        driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
        driver.get(URL_HP)
        try:
            bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        print("Bannery jsou zobrazeny")

                    else:
                        print("neco je spatne ")
                        self.fail()
        except NoSuchElementException:
            print("Bannery se nezobrazují")
            self.fail()
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
                        self.fail()

        except NoSuchElementException:
            print("Nejlepsi nabidky LM se neukazuji")
            self.fail()
        try:
            switchButton = driver.find_element_by_xpath("//*[@class='f_switch-button']")
            driver.execute_script("arguments[0].click();", switchButton)
            time.sleep(4)

        except NoSuchElementException:
            print("nenasel se switchbutton")
            self.fail()

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
                        self.fail()
        except NoSuchElementException:
            print("Nejlepsi nabidky FM se neukazuji")
            self.fail()
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
                        self.fail()
        except NoSuchElementException:
            print("Top nabídka se nezobrazuje")
            self.fail()

        driver.quit()

    def test_LM(self):
        driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
        driver.get(URL_lm)
        time.sleep(1.5)
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
                            print("Zajzedu se zobrazuje pouze ", pocetZajezdu)
                            self.fail()
                    elif pocetZajezdu == 0:
                        print("velky spatny")
                        self.fail()

                    else:
                        print("neco je spatne ")
                        self.fail()
        except NoSuchElementException:
            print("zajeztdy se nezobrazují")
            self.fail()
        try:
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(1)

        except NoSuchElementException:
            print("nenasel se rozbal")
            self.fail()

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
                        self.fail()
        except NoSuchElementException:
            print("zajeztdy se nezobrazují")
            self.fail()

        driver.quit()

    def test_FM(self):
        driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
        driver.get(URL_FM)
        time.sleep(1.5)
        try:
            zajezdyFMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
            zajezdyFMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
            pocetZajezdu = len(zajezdyFMall)
            print(pocetZajezdu)
            if zajezdyFMsingle.is_displayed():
                for WebElement in zajezdyFMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        print("zajezdy jsou zobrazeny")

                        if not pocetZajezdu == 20:
                            print("Zajzedu se zobrazuje pouze ", pocetZajezdu)
                            self.fail()
                    elif pocetZajezdu == 0:
                        print("velky spatny")
                        self.fail()

                    else:
                        print("neco je spatne ")
                        self.fail()
        except NoSuchElementException:
            print("zajeztdy se nezobrazují")
            self.fail()
        try:
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(1)

        except NoSuchElementException:
            print("nenasel se rozbal")
            self.fail()

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
                        self.fail()
        except NoSuchElementException:
            print("zajeztdy se nezobrazují")
            self.fail()

        driver.quit()

    def test_SDO(self):
        driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
        driver.get(URL_stat)
        try:
            destinaceAll = driver.find_elements_by_xpath("//*[@class='fshr-listTable-item']")
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
                        self.fail()
        except NoSuchElementException:
            print("destinace se nezobrazují")
            self.fail()

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
                        self.fail()
        except NoSuchElementException:
            print("dlazdice foto se nezobrazují")
            self.fail()

        try:
            mapa = driver.find_element_by_xpath("//*[@id='google-map']")
            if mapa.is_displayed():
                print("mapa displaynuta")
            else:
                print("neco je spatne ")
                self.fail()
        except NoSuchElementException:
            print("mapa se nezobrazují")
            self.fail()
        driver.quit()


if __name__ == '__main__':
    unittest.main()
