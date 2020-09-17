import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
	r = requests.get(url) # возвращает обьект из целевой урл в виде текста с тегами
	return r.text

def get_total_pages(html):
	#soup = BeautifulSoup(html, 'lxml')
	#total_pages = soup.find('div', class_='pagination').find('a').text.strip() # найти решение последний тег а в списке(!)
	total_pages = 3
	return int(total_pages) # здесь должна быть правильная функция для определения количества страниц для парсинга(в процессе)

def get_page_data(html):
	soup = BeautifulSoup(html, 'lxml')
	ads = soup.find('ul', class_='content-list content-list_tasks') # ищем нужные данные через библиотеку красивыйсуп
	for ad in ads:
		try:
			title = ad.find('div', class_='task__title').get('title')
		except:
			title = ''
		
		try:
			price = ad.find('span', class_='count').text
		except:
			price = ''
		
		try:
			interes = ad.find('span', class_='params__responses icon_task_responses').text.strip()
		except:
			interes = ''
		
		try:
			views = ad.find('span', class_='params__views icon_task_views').text.strip()
		except:
			views = ''
		
		try:
			hour = ad.find('span', class_='params__published-at icon_task_publish_at').text.strip()
		except:
			hour = ''
		
		try:
			url = 'https://freelance.habr.com' + ad.find('a').get('href')
		except:
			url = ''
		
		data = {'title' : title,
				'price' : price,
				'interes': interes, # формируем словарь передаем ему значения переменных 
				'views' : views,
				'hour' : hour,
				'url' : url
				}
		
		write_csv(data) # записываем с помощью функции 

def write_csv(data):
	with open('freelance.csv', 'a', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow((data['title'],
						data['price'],
						data['interes'],
						data['views'],
						data['hour'],
						data['url']
						))


def main(): # основная функция программы
	url = 'https://freelance.habr.com/tasks?q=python'
	base_url = 'https://freelance.habr.com/tasks?page=' # читаем переменные
	last_url = '&q=python'
	
	total_pages = get_total_pages(get_html(url)) # находим общее количество страниц для парсинга получая ответ записываем в переменную 
	
	for i in range(1, total_pages): # итерируем в цикле
		url_gen = base_url + str(i) + last_url # формируем урл для каждой страницы с помощью переменных
		html = get_html(url_gen) # заворачиваем url_gen  в функцию get_html и передаем результат в переменную html
		get_page_data(html) # запускаем функцию get_page_data передав ей html переменную
	print(total_pages)











if __name__ == '__main__': # точка входа
	main()
