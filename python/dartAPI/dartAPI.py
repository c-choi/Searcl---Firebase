from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import json

authkey = 'e1f4f6db5096bdbe2ad7633c92c5c036ea786f83'
crp_cd = '159910'
start_dt = '20070101'
if crp_cd != '':
    url = 'http://dart.fss.or.kr/api/search.json?auth=' + authkey + '&crp_cd=' + crp_cd + '&start_dt=' + start_dt + '&bsn_tp=A001'
else:
    url = 'http://dart.fss.or.kr/api/search.json?auth=' + authkey
response = urlopen(url)
plain_text = response.read()
soup = BeautifulSoup(plain_text, 'html.parser')
data = json.loads(plain_text)

pprint(data)

# lists = soup.select('dl')
# body_data = {}
#
#
#     def fetch_data():
#         i = 1
#         for list in range(len(lists)-1):
#             try:
#                 print(str(i) + ". " + lists[list].find('a').text.strip())
#                 # body_data[i] = str(i) + ". " + list.find('a').text.strip()
#                 i += 1
#             except:
#                 pass

