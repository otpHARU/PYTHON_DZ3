# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(num):
    fib_list = [1, 0, 1]
    if num <= 0:
        return print('Ошибка! Повторите запрос!')
    elif num == 1:
        print('Список чисел:', fib_list)
    else:
        i = 3
        while i < num * 2:
            negofib_list = fib_list[i - 1] + fib_list[i - 2]
            fib_list.append(negofib_list)
            if len(fib_list) % 4 == 0:
                negofib_list = -fib_list[i] 
            fib_list.insert(0, negofib_list)
            i += 2
        print('Список чисел:', fib_list)

fib(int(input('Укажите размер списка: ')))
