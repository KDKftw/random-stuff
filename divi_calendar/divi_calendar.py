import requests
import time
import PySimpleGUI as sg
from bs4 import BeautifulSoup


url = "https://www.nasdaq.com/market-activity/stocks/orc/dividend-history"
content = requests.get(url).text
#soup = BeautifulSoup(content, "html.parser")

soup = BeautifulSoup(content, "lxml")
#diviHistory = soup.find("td", class_="dividend-history__cell").text
diviHistory = soup.prettify()

print(diviHistory)