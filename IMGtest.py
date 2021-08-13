##tried to test imgs for their response

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")



def test_images_for_200_response():


    driver.get('https://www.eximtours.cz')
    time.sleep(5)
    example_images = driver.find_elements(By.TAG_NAME, 'img')
    example_images2 = driver.find_elements_by_css_selector("img")
    pocetIMG = len(example_images)
    pocetIMG2 = len(example_images2)
    print(pocetIMG)
    print(pocetIMG2)

    ##for image in example_images:
      ##  current_link = image.get_attribute("src")
       ## r = requests.get(current_link)
       ## try: self.assertEqual(r.status_code, 200)
      ##  except AssertionError as e: self.verificationErrors.append(current_link + ' delivered response code of ' + r.status_code)


test_images_for_200_response()