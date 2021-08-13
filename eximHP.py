##request try

from selenium import webdriver



URL = "https://www.eximtours.cz/"


def test():
    driver = webdriver.Chrome(executable_path=r"C:\Users\KDK\Desktop\ChromeDriver\chromedriver.exe")
    driver.get(URL)

    for request in driver.requests:
        if request.response:
            print(
                request.url,
                request.response.status_code,
                request.response.headers['Content-Type']
            )




test()