# from bs4 import BeautifulSoup
# import requests
#
#
# source = requests.get("https://www.delfi.lt/").text
# print(source)
#
#
#
# # blokas = soup.find('div', class_ = 'headline')
# # print(blokas.prettify()


#
# from bs4 import BeautifulSoup
# import requests
#
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokas = soup.find('div', class_ = 'headline')
#
# kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#
# tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
# print(kategorija)
# print(tekstas)

#
#
# from bs4 import BeautifulSoup
# import requests
#
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all(class_ = 'headline')
#
# for blokas in blokai:
#     try:
#         kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#         tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#         print(kategorija)
#         print(tekstas)
#     except:
#         pass

# #
# from bs4 import BeautifulSoup
# import requests
# import csv
#
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')
#
# with open("delfi naujienos.csv", "w", encoding="UTF-8", newline='') as failas:
#
#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Kategorija', 'Tekstas'])
#     for blokas in blokai:
#         try:
#             kategorija = blokas.find('div', class_ = 'headline-category').text.strip()
#             tekstas = blokas.find('a', class_ = 'CBarticleTitle').text.strip()
#             csv_writer.writerow([kategorija, tekstas])
#         except:
#             pass
#
#
# #
# from bs4 import BeautifulSoup
# import requests
#
# source = requests.get('https://www.delfi.lt/').text
# soup = BeautifulSoup(source, 'html.parser')
# blokai = soup.find_all('div', class_ = 'headline')
#
# print(blokai[:2])
#
#
#
#

import csv

from bs4 import BeautifulSoup
import requests

source = requests.get('https://shop.telia.lt/telefonai/?filter=brand:samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_='card card__product card--anim js-product-compare-product')



for blokas in blokai:
    print(blokas.text.strip())
