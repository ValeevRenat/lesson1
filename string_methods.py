#Вывести количество символов введённого текста
my_string = str(input("Введите строку: "))
print(len(my_string))

###############Работа с методами строк###############

#Выведите строку my_string в верхнем регистре.
string = input('Введите текст для изменения на верхний регистр: ')
print(string.upper())

#Выведите строку my_string в нижнем регистре.
string = input('Введите текст для изменения на нижний регистр: ')
print(string.lower())

#Измените строку my_string, удалив все пробелы.
string = input('Введите текст для удаления пробелов: ')
print(string.replace(" " , ""))


#Выведите первый символ строки
string = input('Введите данные для вывода первого символа строки: ')
print(string[0])

#Выведите поледнего символа строки
string = input('Введите данные для вывода последнего символа строки: ')
print(string[-1])


