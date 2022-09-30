# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).

from random import sample

def num_list(count):
    if count <= 0:
        return print("Ошибка! Повторите запрос!")
    my_list = sample(range(1, count * 2), count)
    print(f'Список элементов:', my_list)
    summ = 0
    for i in range(count):
        if i % 2 == 0:
            summ += my_list[i]
    print(f'Сумма элементов на нечетных позициях:', summ)

num_list(int(input('Укажите количество элементов в списке: ')))