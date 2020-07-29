import re


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
print(list_imp)
print('Среднее значение ', round(medium), 'рублей')
