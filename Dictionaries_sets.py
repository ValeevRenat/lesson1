my_dict = {'Vasya' : 1990 , 'Mark': 1993, 'Olga' : 2005}
print('Словарь:', my_dict)
x = ('Год рождения Vasya :' , my_dict['Vasya'])
x = ('Год рождения Vasya :' , my_dict.get('Vasya', 'Неизвестно'))
my_dict.update({'Vasya':1991})
removed_year = my_dict.pop('Olga')
print('Удаленный год рождения \'Olga\':', removed_year)
print('Измененный словарь', my_dict)


set = {1, 2, 3, 4, 5, 6, 7, 20, True, 'Hello'}
print('Множество:', set)
set.add('11')
set.add('99')
set.remove("Hello")
print('Измененное множество:' , set)
