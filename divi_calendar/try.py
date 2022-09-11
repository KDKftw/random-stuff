import requests
from bs4 import BeautifulSoup

URL_ORC = "https://www.dividend.com/stocks/financials/specialty-finance/mortgage-finance/orc-orchid-island-capital-inc/"
URL_ARR = "https://www.dividend.com/stocks/financials/specialty-finance/mortgage-finance/arr-armour-residential-reit-inc/"
URL_HRZN = "https://www.dividend.com/stocks/financials/asset-management/investment-management/hrzn-horizon-technology-finance-corp/"

content = requests.get(URL_HRZN).text
soup = BeautifulSoup(content, "html.parser")

diviHistory = soup.findAll("div", class_="t-flex t-text-lg t-font-medium t-leading-tighter t-h-5 t-mt-1 t-mb-3 md:t-mt-1 md:t-mb-1")

print(diviHistory)
print(diviHistory[1].text)


def nextDiviDate(URL, ticker):
    content = requests.get(URL).text
    soup = BeautifulSoup(content, "html.parser")
    diviHistory = soup.findAll("div",
                               class_="t-flex t-text-lg t-font-medium t-leading-tighter t-h-5 t-mt-1 t-mb-3 md:t-mt-1 md:t-mb-1")
    diviPaymentDate = diviHistory[1].text
    print(diviPaymentDate, ticker)
    return(diviPaymentDate, ticker)

nextDiviDate(URL_ORC, "ORC")