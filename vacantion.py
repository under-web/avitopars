import requests
from bs4 import BeautifulSoup
import csv

def get_html(url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
    r = requests.get(url, headers=headers, timeout=5)
    if r.status_code == 200:
        print('Ок!')
 
    elif r.status_code == 404:
        print('Страница не существует!')
    return r.text

def write_csv(data):
	with open('vacantion.csv', 'a', encoding='utf8') as f:
		writer = csv.writer(f, delimiter='|')
		writer.writerow((data['title'],
						data['price'],
						data['link']))

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	block = soup.find('div', class_='snippet-list js-catalog_serp')
	for i in block:

		
			try:
				title = i.find('a', class_='snippet-link').get("title").strip()
				if 'приёмщик' in title:
					continue
				elif 'ключей' in title:
					continue
				elif 'одежды' in title:
					continue
				elif 'вмятин' in title:
					continue
				elif 'Отделочник' in title:
					continue
				else:
					pass
				

			except:
				title = ''
			
			

			try:
				price = i.find('span', class_='snippet-price').text.strip()
			except:
				price = ''


			try:
				link = i.find('a', class_='snippet-link').get("href")
			except:
				link = ''

			print(title + '\n', price + '\n', link + '\n')
			data = {'title':title,
					'price':price,
					'link':link}
			write_csv(data)


def main():

	url = 'https://www.avito.ru/kazan/vakansii?q=%D0%BC%D0%B0%D1%81%D1%82%D0%B5%D1%80+%D1%80%D0%B5%D0%BC%D0%BE%D0%BD%D1%82%D0%B0'
	html = get_html(url)
	get_page_data(html)
	input()



if __name__ == '__main__':
	main()