import requests
from bs4 import BeautifulSoup
import csv

#url = 'https://www.avito.ru/kazan?q=%D0%BC%D1%91%D0%B4' #целевая страница

def get_html(url):
	r = requests.get(url)
	return r.text

def get_total_pages(html):
	#total_pages = 'https://www.avito.ru/kazan?q=%D0%BC%D1%91%D0%B4&p=5'
	total_pages = 5
	return int(total_pages)

def write_csv(data):
	with open('avito.csv', 'a', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],
						data['price'],
						data['url']))

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('div', class_='js-catalog_serp').find_all('div', class_='item_table')
	for ad in ads:
		try:
			title = ad.find('div', class_='description.item_table-description').find('h3').text.strip()
			
		except:
			title = 'none'
		try:
			url = 'https://www.avito.ru' + ad.find('div', class_='description.item_table-description').find('a').get('href')
		except:
			url = 'none'
		try:
			price = ad.find('span', class_='snippet-price').text.sprip()
		except:
			price = 'none'
			
		data = {'title':title,
				'price':price,
				'url':url}
		write_csv(data)

def main():
	url = 'https://www.avito.ru/kazan?q=%D0%BC%D1%91%D0%B4&p=5'
	base_url = 'https://www.avito.ru/kazan?q=мёд&'
	page_part = 'p='
	
	total_pages = get_total_pages(get_html(url))
	
	for i in range(1, total_pages):
		url_gen = base_url + page_part + str(i)
		html = get_html(url_gen)
		get_page_data(html)
		print(url_gen)
		

if __name__ == '__main__':
	main()
