from urllib.request import urlopen
from bs4 import BeautifulSoup

for g in (economy, society, culture, diplomacy):

    url = 'http://www.korea.kr/policy/' + 'List.do'
    response = urlopen(url)
    plain_text = response.read()
    soup = BeautifulSoup(plain_text, 'html.parser')

    lists = soup.select('dl')
    body_data = {}


    def fetch_data():
        i = 1
        for list in range(len(lists)-1):
            try:
                print(str(i) + ". " + lists[list].find('a').text.strip())
                # body_data[i] = str(i) + ". " + list.find('a').text.strip()
                i += 1
            except:
                pass

    # print(body_data)

    # fetch_data()