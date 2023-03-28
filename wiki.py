from urllib.request import urlopen
from bs4 import BeautifulSoup

#we will scrape for data about populations in countries
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
response = urlopen(url)

soup = BeautifulSoup(response, "html.parser")

#get second table, the first one has non relevant data
table = soup.find_all("table")[1]

populations = {}

for row in table.find_all("tr"):
    #skip first row with data for whole world
    if "World" in row.get_text(): continue

    cells = row.find_all("td")
    if len(cells) >= 2:
        country = cells[0].get_text().strip()
        population = int(cells[1].get_text().strip().replace(",", ""))
        populations[country] = population

#print top 10 countries
print("Top 10 countries by population:")
for country, population in list(populations.items())[:10]:
    print(f"{country + ':':20}{population:>15,}")