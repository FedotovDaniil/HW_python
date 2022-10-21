import random

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
'''
def fill_list():
    list = []
    for i in range(7):
        list.append(random.randint(1, 10))
    return list

def number_multiply(list):
    for i in range(int(len(list)/2)):
        print(list[i] * list[-i - 1])
    if len(list) % 2 == 1:
        print(list[int(len(list) / 2)] ** 2) 
        

 
list = fill_list()
print(list)
number_multiply(list)

''' 
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19



def fill_list():
    list = []
    for i in range(7):
        list.append(random .uniform(1, 10))
    return list

def fraction_difference(list):
    min = 1
    max = 0
    
    for i in list:
        list[i] % i
        if list[i] < min:
            min = list[i]
        if list[i] > max:
            max = list[i]

list = fill_list()
print(format(list, '.2f'))


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке
