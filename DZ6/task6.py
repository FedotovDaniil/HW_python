# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]

# def get_double():
#     numbers = list(map(int, input("Введите числа ---> ").split()))
#     return " ".join(map(str, filter(lambda i: 9 < abs(i) < 100, numbers)))

# print(get_double())


# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

# unfiltered_str = [12,'sadf',5643]
# result = list(filter(lambda i: type(i) == int, unfiltered_str))
# result2 = list(filter(lambda i: type(i) == str, unfiltered_str))

# print(f'Числа: {result}')
# print(f'Строки: {result2}')



# # Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, List Comprehension
# # 3) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# # Пример:
# # - 6782 -> 23
# # - 0, 56 -> 11

# def real_sum(num):
#     return sum(map(int, num.replace('.','').replace('-','')))

# num  = input('Введите вещественное число ---> ')
# print(f'Сумма ---> {real_sum(num)}')