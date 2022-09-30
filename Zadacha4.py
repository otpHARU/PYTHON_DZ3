# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.


from random import uniform

def num_list(count):
    list1 = list()
    if count <= 0:
        return print("Ошибка! Повторите запрос!")
    for i in range(count):
        num = round(uniform(1, 10), 2)
        list1.append(num)
    print('Список чисел:', list1)
    min = 1
    max = 0
    dif = 0
    for i in range(count):
        if (list1[i] % 1) < min:
            min = round((list1[i] % 1), 2)
        if (list1[i] % 1) > max:
            max = round((list1[i] % 1), 2)
    dif = round(max - min, 2)
    print('Минимальное значение:', min, '\nМаксимальное значение:', max, '\nРазница значений:', dif)

num_list(int(input('Укажите количество элементов в списке: ')))


























