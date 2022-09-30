# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(num):
    if num <= 0:
        return 'Ошибка! Повторите запрос!'

    fib_list = [0, 1]

    for i in range(1, num):
        fib_list.append(fib_list[i] + fib_list[i - 1])

    negofib_list = fib_list[::-1]

    for i in range(0, num - 1, 2):
        negofib_list[i] = -negofib_list[i]

    negofib_list.pop(num)
    print('Список чисел:', negofib_list + fib_list)

fib(int(input('Укажите размер списка: ')))




