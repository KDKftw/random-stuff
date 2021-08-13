##just a request code
import requests

r = requests.get('https://www.eximtours.cz/searchresult/getlmhotels?DS=1024&TO=4312&D=64092&DD=2021-02-13&RD=2021-02-20&ER=0&NN=7&PF=0&PT=900000&AC1=2&KC1=0&IC1=0&QF=108_1_0&pITG=5')
print(r.status_code)

s = requests.get("https://www.eximtours.cz/api/PriceCheck/GetPrices")
print(s.status_code)
