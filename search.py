from bs4 import BeautifulSoup
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/80.0"
query = "site:in.linkedin.com inurl:\".com/in/\" \"some text\"" #   REMEMBER TO URL ENCODE THE POUND SIGN AS %23
#query = query.replace(' ', '+')
#Loop for scraping all of the google results sites
for x in range(1, 1000, 10):
    URL = f"https://google.com/search?q={query}&start={x}"
    headers = {"user-agent": USER_AGENT}
    resp = requests.get(URL, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        results = []
        for g in soup.find_all('div', class_='rc'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        for x in results:
            print(x)
    else:
        print(resp.status_code)