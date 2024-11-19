from bs4 import BeautifulSoup
import lxml
import requests

# url = 'https://myfin.by/currency/minsk'
#
# page = requests.get(url)
# page = page.text
#
# with open ('pars.html', 'w', encoding='utf-8') as file:
#     file.write(page)

with open('pars.html', encoding='utf-8') as file:
    src = file.read()

second = ''
soup = BeautifulSoup(src, 'lxml')

dashboard = soup.find_all(class_="course-brief-info__b")


lst = [dashboard[3].text, dashboard[4].text, dashboard[6].text, dashboard[7].text, dashboard[9].text, dashboard[10].text]
print(lst)








