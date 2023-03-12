import requests
result=requests.get("https://en.wikipedia.org/wiki/Vikram_Sarabhai")


import bs4
tex=bs4.BeautifulSoup(result.text,"lxml")
print(tex.select('.thumbcaption')[1].text)

