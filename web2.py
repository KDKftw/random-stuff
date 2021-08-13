##set of tests

import time
import unittest
from email.mime.text import MIMEText

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.eximtours.cz"
URL_lm = "https://www.eximtours.cz/last-minute"
URL_fm = "https://www.eximtours.cz/first-minute"
URL_stat = "https://www.eximtours.cz/recko"
driver = webdriver.Ie(executable_path=r"C:\Users\KDK\Desktop\IEdriver\IEDriverServer.exe")
wait = WebDriverWait(driver, 25)
cisloNodu = "SRWEB2"
import smtplib, ssl


def email(msg):
    fromx = 'alertserverproblem@gmail.com'
    to = 'ooo.kadoun@gmail.com'
    msg = MIMEText(msg)
    msg['Subject'] = "SRWEB2"
    msg['From'] = fromx
    msg['To'] = to

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login("alertserverproblem@gmail.com", "xx")
    server.sendmail(fromx, to, msg.as_string())
    server.quit()


class TEST(unittest.TestCase):

    def test_SearchDetail(self):
        driver.get(URL)
        driver.maximize_window()
        try:
            lmZajezdNej = driver.find_element_by_xpath(
                "//*[@class='f_tourTable-tour-item f_tourTable-tour-item--destination']")
            wait.until(EC.visibility_of(lmZajezdNej))
            lmZajezdNej.click()
        except NoSuchElementException:
            x = " Problém HP-Nej. nabidka - nenašel se LM zájezd"
            email("Problém HP-Nej. nabidka - nenašel se LM zájezd")
            self.fail()

        time.sleep(3)

        try:
            hotelySingle = driver.find_element_by_xpath("//*[@id='divHotelCard']")
            hotelyAll = driver.find_elements_by_xpath("//*[@id='divHotelCard']")
            wait.until(EC.visibility_of(hotelySingle))
            if hotelySingle.is_displayed():
                for WebElement in hotelyAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        x = " Problém s hotely v searchi - hotelCard "
                        email(x)
        except NoSuchElementException:
            x = cisloNodu, "Problém s hotely v searchi - hotelCard "
            email(x)
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
                        x = " SRWEB2 Problém s fotkami hotelů v searchi "
                        email(x)
                        self.fail()
        except NoSuchElementException:
            x = cisloNodu + "  Problém s fotkami hotelů v searchi "
            email(x)
            self.fail()

        try:
            cenaAll = driver.find_elements_by_xpath("//*[@class='fshr-searchResult-item-summary']")
            cenaSingle = driver.find_element_by_xpath("//*[@class='fshr-searchResult-item-summary']")
            wait.until(EC.visibility_of(cenaSingle))
            if cenaSingle.is_displayed():
                for WebElement in cenaAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        x = " SRWEB2 Problém s cenami hotelů v searchi "
                        email(x)
                        self.fail()

        except NoSuchElementException:
            x = "SRWEB2 Problém s cenami hotelů v searchi "
            email(x)
            self.fail()

        try:
            detailHotelu = driver.find_element_by_xpath("//*[@class='fshr-bubble-wrapper']")
            wait.until(EC.visibility_of(detailHotelu))
            detailHotelu.click()


        except NoSuchElementException:
            x =  " SRWEB2   Neprokliknutí detailu hotelu ze search "
            email(x)
            self.fail()

        time.sleep(1)
        driver.switch_to.window(driver.window_handles[-1])

        try:
            detailFotka = driver.find_element_by_xpath("//*[@class='fshr-detailGallery']")
            wait.until(EC.visibility_of(detailFotka))
            if detailFotka.is_displayed():
                pass
        except NoSuchElementException:
            x = "SRWEB2 Problém s fotkami na detailu hotelu "
            email(x)
            self.fail()

        try:
            sedivka = driver.find_element_by_xpath("//*[@class='fshr-detail-summary js-detailSummary']")
            wait.until(EC.visibility_of(sedivka))
            if sedivka.is_displayed():
                pass


        except NoSuchElementException:
            x ="SRWEB2 Problém se šedivkou na detailu hotelu "
            email(x)
            self.fail()
        try:
            terminyCeny = driver.find_element_by_xpath("//*[@id='terminyaceny-tab']")
            wait.until(EC.visibility_of(terminyCeny))
            terminyCeny.click()
            potvrdit = driver.find_element_by_xpath(
                "//*[@class='fshr-button fshr-button--commonImportance fshr-button--big js-popupWindow--close']")
            driver.execute_script("arguments[0].click();", potvrdit)
        except NoSuchElementException:
            x = "SRWEB2 Problém přepnutí na termíny a ceny na detailu hotelu "
            email(x)

        try:
            terminySingle = driver.find_element_by_xpath("//*[@data-hotel]")
            wait.until(EC.visibility_of(terminySingle))

            if terminySingle.is_displayed():
                pass
            else:
                x = "SRWEB2 Problém s termíny a ceny na detailu hotelu "
                email(x)
                self.fail()

        except NoSuchElementException:
            x = "SRWEB2 Problém s termíny a ceny na detailu hotelu "
            email(x)
            self.fail()

    def test_HomePage(self):
        driver.get(URL)
        try:
            bannerSingle = driver.find_element_by_xpath("//*[@class='f_teaser-item']")
            bannerAll = driver.find_elements_by_xpath("//*[@class='f_teaser-item']")
            wait.until(EC.visibility_of(bannerSingle))
            if bannerSingle.is_displayed():
                for WebElement in bannerAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        x = cisloNodu + "Problém na HP s bannery "
                        email(x)
                        self.fail()
        except NoSuchElementException:
            x = """\
Subject: SRWEB2 

Problém na HP s bannery """
            email(x)
            self.fail()
        time.sleep(1.5)
        try:
            nejnabidkyLMsingle = driver.find_element_by_xpath("//*[@class='f_tourTable-tour']")
            nejnabidkyLMall = driver.find_elements_by_xpath("//*[@class='f_tourTable-tour']")
            if nejnabidkyLMsingle.is_displayed():
                for WebElement in nejnabidkyLMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
                    else:
                        x = """\
Subject: SRWEB2 

Problém na HP s nej. nabídky LM """
                        email(x)
                        self.fail()

        except NoSuchElementException:
            x = """\
Subject: SRWEB2 

Problém na HP s nej. nabídky LM """
            email(x)
            self.fail()
        try:
            switchButton = driver.find_element_by_xpath("//*[@class='f_switch-button']")
            driver.execute_script("arguments[0].click();", switchButton)
            time.sleep(2.5)

        except NoSuchElementException:
            x = """\
Subject: SRWEB2 

Problém s HP - switch button u nej. nabídky """
            email(x)
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
                        x = """\ Subject: SRWEB2 

                                                                                                                                                                                    Problém s homepage -  FM nejlepsi nabidky nabídkou """
                        email(x)
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
                        pass
                    else:
                        x = """\
                                                                                                                                                                                    Subject: SRWEB2 

                                                                                                                                                                                    Problém na HP - top nabídky """
                        email(x)
                        self.fail()
        except NoSuchElementException:
            x = """\
                                                                                                                                                                                                Subject: SRWEB2 

                                                                                                                                                                                                Problém na HP - top nabídky """
            email(x)
            self.fail()

    def test_LM(self):
        ##driver.get(URL_lm)
        driver.get("file:///C:/Users/KDK/Desktop/Last minute_ čerstvá nabídka, vysoké slevyLM18.html")
        try:
            zajezdyLMsingle = driver.find_element_by_xpath("//*[@class='page-tour']")
            zajezdyLMall = driver.find_elements_by_xpath("//*[@class='page-tour']")
            if zajezdyLMsingle.is_displayed():
                for WebElement in zajezdyLMall:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass

                    else:
                        msg = "SRWEB2 Problem s LM  zajezdy se neukazuji "
                        email(msg)
                        self.fail()
        except NoSuchElementException:
            print("no such")
            msg = "SRWEB2 Problem s LM  zajezdy se neukazuji "
            email(msg)
            self.fail()
        try:
            rozbal = driver.find_element_by_xpath("//*[@class='page-tour-cell page-tour-control']")
            driver.execute_script("arguments[0].click();", rozbal)
            time.sleep(1)

        except NoSuchElementException:
            msg = "SRWEB2 Nepodarilo se rozbalit LM zajezd "
            email(msg)
            self.fail()

        try:
            rozbalenyZajezd = driver.find_element_by_xpath("//*[@class='page-tour-hotel-name']")
            rozbalenyZajezdAll = driver.find_elements_by_xpath("//*[@class='page-tour-hotel-name']")
            if rozbalenyZajezd.is_displayed():
                for WebElement in rozbalenyZajezdAll:
                    jdouvidet = WebElement.is_displayed()
                    if jdouvidet == True:
                        pass
        except NoSuchElementException:
            msg = "SRWEB2  "
            email(msg)
            self.fail()

    def test_FM(self):
        driver.get(URL_fm)
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

    def test_SDO(self):
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


if __name__ == '__main__':
    unittest.main()
