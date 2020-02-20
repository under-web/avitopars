import requests
from bs4 import BeautifulSoup
url = 'https://www.avito.ru/kazan?q=%D0%BC%D1%91%D0%B4' #целевая страница

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml') # выбрали парсер

page = soup.find_all('div', class_= 'item_table-header') # ищем заголовки с текстом содержащим название обьявления и цену
lin = soup.find_all('a' , class_ = 'snippet-link') # ищем в другом разделе все ссылки

#print(lin)
for div in page: #создаем цикл для всех div в объекте супа page
	name_title = div.get_text() # создали переменную переали ей текст мз div

for a in lin: # создали цикл для а в lin 
	links = a.get('href')


with open('avito.txt', 'a', encoding='utf8') as info:
	for d in name_title:
		info.write(name_title)
		for t in links:
			info.write(links)
		#print(name_title, 'https://www.avito.ru' + links)


print(len(links))
