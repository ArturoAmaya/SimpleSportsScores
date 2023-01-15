import requests
from bs4 import BeautifulSoup
leagues_I_want = ["English Premier League", "Spanish LaLiga", "Italian Serie A", "French Ligue 1"]
# Make the GET
r = requests.get("https://www.espn.com/soccer/schedule")

# checks status
print(r)


soup = BeautifulSoup(r.content, 'html.parser')
leagues_html = []

leagues = soup.find_all('div', class_='responsive-table-wrap scoreboard-table-header')
league_headers = soup.find_all('h2', class_='table-caption date-header-caption')
for i in range(0,len(league_headers)):
    if league_headers[i].text in leagues_I_want:
        leagues_html.append( leagues[i] )

print(leagues_html)

Func = open("index.html","w")
Func.write("<!doctype html>\n<html>\n<head>\n<link rel='stylesheet' href='styles.css'>\n<title>Top Five Leagues</title>\n</head>\n<body>")
for item in leagues_html:
    Func.write(str(item))
    Func.write("\n")
Func.write("</body>\n</html>")

Func.close()
