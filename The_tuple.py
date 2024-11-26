#- Создайте переменную immutable_var
#- Выполните операции вывода кортежа immutable_var на экран

immutable_var = 1, 2.0, 3, [1, 2.0, 3], "False"
print(immutable_var)

# попробуем изменить один из его элементов

#immutable_var = 1, 2.0, 3, [1, 2.0, 3], "False"
#print(immutable_var)[0] = 4  # кортежи являются неизменяемыми это свойство кортежей

mutable_list = ( 1, 2, 'a', 'b')
mutable_list = list(mutable_list)
print(mutable_list)

#Создание изменяемых структур данных
mutable_list = [1, 2, 'a', [1, 2, 3.0, 4], False]
mutable_list[0] = 'one'
mutable_list[1] = 10
print(mutable_list)
