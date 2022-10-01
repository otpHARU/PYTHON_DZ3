# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from random import sample

def list_int(count):
    if count <= 0:
        return 'Ошибка!'
    list2 = sample(range(1, count * 3), count)
    return list2

def prod_num(list3):
    gen = 0
    length = len(list3)
    gen_list = []
    for i in range(length // 2):
        gen = list3[i] * list3[length - i - 1]
        gen_list.append(gen)
    if length % 2:
        gen_list.append(list3[length // 2])
    # print('Произведение чисел:', gen_list)
    return gen_list

list1 = list_int(int(input('Укажите количество элементов в списке: ')))
if list1 != 'Ошибка!':
    print ('Список элементов:', list1)
    print('Произведение пар чисел:', prod_num(list1))
else:
    print('Ошибка! Повторите запрос!')

