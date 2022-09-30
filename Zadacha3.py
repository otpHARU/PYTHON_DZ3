# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.

def num_transform(count):
    if count <= 0 or count > 65536:
        return print("Неверное значение! Повторите запрос.")
    num = 0
    res = 0
    while count > 0:
            for i in range(count):
                num = (count % 2) * 10 ** i
                res += num
                count //= 2
    print('Двоичное число:', res)

num_transform(int(input('Введите чиcло: ')))

























