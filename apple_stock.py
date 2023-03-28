import urllib.request
from bs4 import BeautifulSoup

#we will scrape Apple stock price
url = "https://finance.yahoo.com/quote/AAPL/history"

# data couldnt be loaded without user agent
req = urllib.request.Request(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    })
response = urllib.request.urlopen(req)
soup = BeautifulSoup(response.read(), "html.parser")

#find specific table
table = soup.find("table", class_="W(100%) M(0)")
rows = table.find_all("tr")

print("Printing historical closing price for Apple stock:")
#skip first and last line (first has column titles, last has some disclaimers)
for row in rows[1:-1]:
    columns = [col.get_text() for col in row.find_all("td")]
    if len(columns) == 7:
        print(f"{columns[0]}:  ${columns[4]}")