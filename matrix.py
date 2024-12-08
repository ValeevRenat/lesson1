def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Кол-во строк матрицы    :'))
m = int(input('Кол-во столбцов матрицы :'))
value = input(f'Задайте значения матрицы : ')
print('-------' * m)
matrix = get_matrix(n, m, value)

if n <= 0:
    print("Задано неверное количество строк:", n)
elif m <=0:
    print("Задано неверное количество столбцов:" ,m)
else:
    print("Матрица:")
    for i in matrix:
        print(*i)