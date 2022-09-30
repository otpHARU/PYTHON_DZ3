# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import sample

def num_list(count):
    if count < 0:
        return print("Ошибка! Повторите запрос!")
    list1 = sample(range(1, 10), count)
    print('Список элементов:', list1)
    list2 = list()
    for i in range(count // 2):
        gen = list1[i] * list1[(i + 1) * -1]
        list2.append(gen)
    print('Произведение пар чисел:', list2)

num_list(int(input('Укажите количество элементов в списке: ')))
