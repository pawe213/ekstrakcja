import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.formula1.com")
pageRootElement = BeautifulSoup(response.text, 'html.parser')

for header in pageRootElement.select('.f1-cc--caption'):
    children = header.children
    for child in children:
        try:
            if "no-margin" in child['class']:
                print(child.text)
        except:
            pass

# getting results for every race

response = requests.get("https://www.formula1.com/en/results.html/2018/races.html")
pageRootElement = BeautifulSoup(response.text, 'html.parser')

tabelka = pageRootElement.select('.ArchiveLink')
domena = 'https://www.formula1.com'
adresy_wynikow = {}
for row in tabelka:
    link = row.attrs['href']
    country = row.contents[0].strip()
    adresy_wynikow[country] = domena + link


for key, value in adresy_wynikow.items():
    print(key, value)
    race_response = requests.get(value)
    pageRootElementRace = BeautifulSoup(race_response.text, 'html.parser')
    race_score = pageRootElementRace.select('.resultsarchive-col-right')
    for child in race_score[0].select('tbody tr'):
        print(child)
