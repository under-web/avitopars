import requests
from bs4 import BeautifulSoup
import csv
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(dany):
	with open('avito_room.csv', 'a', encoding='utf8') as f:
		writer = csv.writer(f)
		writer.writerow((dany['title'],
						dany['price'],
						dany['adress'],
                         dany['hour'],
                         dany['link']))

def get_page_data(html):
    l = 0

    soup = BeautifulSoup(html, 'lxml')
    data = soup.find('div', class_='snippet-list js-catalog_serp')
    for i in data:
        try:
            title = i.find('a', class_='snippet-link').get("title").strip()
            if 'в Бугульме' in title: # Проверяем в названии обьявления чтобы был нужный город
                pass # Продолжается работа скрипта

            else:
                break # Иначе прерывает цикл
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


        if title == '': # Возник баг с повторением исключения в итоге печаталось всюду https://www.avito.ru
            continue # теперь встречая эксепт с пустым значением переходит занаво цикл не доходя до принта
        else:
            l = l + 1
            print(title, price, adress, hour, 'https://www.avito.ru' + link + '\n')
            dany = {'title':title,
                    'price':price,
                    'adress':adress,
                    'hour':hour,
                    'link':link}
            write_csv(dany)
    print('Всего обьявлений', l)

    
def get_pars():
    data_analiz = open('avito_room.csv', encoding='utf8').read()


    list_4 = re.findall(r'\d\s\d\d\d', data_analiz) # Находит число 4 х значное с пробелом
    list_5 = re.findall(r'\d\d\s\d\d\d', data_analiz)# Находит число 5 и значное с пробелом
    list_4.extend(list_5) # объединение списков 
    list_imp = []

    for i in list_4:
        j = i.replace(' ', '')# в элементах списка удаляем пробелы
        j = int(j)# преобразуем элементы из str() в int()
        if j != 0:# Если значение не равно нулю добавляем в конечный список
            list_imp.append(j)

    medium = sum(list_imp) / len(list_imp)  
    medium = round(medium)

    with open('data_base.txt', 'a', encoding='utf8') as f:
        f.write(str(medium) + '\n')
    print('Среднее значение ', medium, 'рублей')
    input()

    

def main():
    url = 'https://www.avito.ru/bugulma/kvartiry/sdam/2-komnatnye-ASgBAQICAUSSA8gQAUDMCBSQWQ?cd=1&f=ASgBAQICAkSSA8gQ8AeQUgFAzAgUkFk'
    html = get_html(url)
    get_page_data(html)
    get_pars()







if __name__ == '__main__':
	main()
