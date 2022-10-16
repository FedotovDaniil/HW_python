# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def Factorial(x):
#     multiply = 1
#     result = []
#     for i in range(1,x+1):
#         multiply *= i
#         result.append(multiply)
#     return result


# def Print_count(N):
#     count = '('
#     for i in range(1, N + 1):
#         if i != 1:
#             count += ", "
#         for j in range(1, i + 1):
#             count += str(j)
#             if j != i:
#                 count += '*'
#     count += ")"
#     return count


# N = int(input('Пусть N = '))
# result = Factorial (N)
# count = Print_count(N)
# print("тогда", result, count)

# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

# Пример:

# - Для n = 15:  Ответ: 3
# - Для n = 35:  Ответ: 5

# a = int(input())
# num = 2 
# while a % num != 0: 
#     num +=1
    
# print(num)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных ИНДЕКСАХ. Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 4, 3, 1, 8]
# Ввод: 10
# [-10, -9, ...-4, -3, -2, -1, 0, 1, 2, 3,4....10]

a = int(input("a = "))
indexes = [4, 1, 6, 10, 8]
arr = []
for i in range(-a, a+1):
    arr.append(i)
a = 1
for i in indexes:
    a *= arr[i]
print(arr, "\n", a) 

# Требуется посчитать сумму чётных чисел, расположенных между числами 1 и N включительно.

a = int(input())
c = 0
for i in range(a + 1):
    if i % 2 == 0:
        c += i
print(c)