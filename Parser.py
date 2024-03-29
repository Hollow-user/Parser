
import requests
from bs4 import BeautifulSoup as bs

headers = {'accept': '*/*',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Safari/537.36'}

base_url = 'https://www.avito.ru/habarovsk/igry_pristavki_i_programmy/igrovye_pristavki?cd=1'

items = []     # Словарь для сбора данных с парсера


def start_pars(base_url, headers):
    """
    Основная функция для парсинга
    :param base_url: урл сайта что будет проходить парсер
    :param headers: данные о пользователе, чтобы сайт не блокировал как бота
    :return:
    """
    session = requests.Session()
    request = session.get(base_url, headers=headers)

    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'item item_table clearfix js-catalog-item-enum item-with-contact js-item-extended'})
        for div in divs:
            title = div.find('a', attrs={'class': 'item-description-title-link'}).text
            href = div.find('a', attrs={'class': 'item-description-title-link'})['href']
            items.append({
                'title': title,
                'url': 'https://www.avito.ru{}'.format(href)
            })
    else:
        print('ERROR')


start_pars(base_url, headers)

for item in items:
    print(item['title'], item['url'])

