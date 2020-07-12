import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_='snippet-list js-catalog_serp')
    for i in data:
        try:
            title = i.find('a', class_='snippet-link').get("title").strip()
            if 'в Бугульме' in title:
                pass
            else:
                break
	
        except:
            title = ''




        try:
            price = i.find('span', class_='snippet-price').text.strip()
        except:
            price = ''
        try:
            adress = i.find('span', class_='item-address__string').text.strip()
        except:
            adress = ''
        try:
            hour = i.find('div', class_='snippet-date-info').text.strip()
        except:
            hour = ''
        try:
            link = i.find('a', class_='snippet-link').get("href")
        except:
            link = ''
        print(title, price, adress, hour, 'https://www.avito.ru' + link + '\n' )


def main():
    url = 'https://www.avito.ru/bugulma/kvartiry/sdam/2-komnatnye-ASgBAQICAUSSA8gQAUDMCBSQWQ?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgUkFk'
    html = get_html(url)
    get_page_data(html)








if __name__ == '__main__':
	main()
