# # Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# # Пример:

# # - 6 -> да
# # - 7 -> да
# # - 1 -> нет

# # from re import X
# # from tkinter import Y


# a = int (input("Введите день недели ->"))
# if 1 <= a <= 5:
#      print(a,"- будний день")
# if 6 <= a <=7:
#      print(a, "- выходной день")
    
# # Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Примечание:
# # Используйте знания об Алгебра Логике, вы должны перебрать все возможные комбинации значений X, Y, Z (принимают значения 0 или 1)

# X = input("ввеедите x = ")
# Y = input("ввеедите y = ")
# Z = input("ввеедите z = ")

# print(not (X or Y or Z) == (not X and not Y and not Z))

# # Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# # Пример:

# # - x=34; y=-30 -> 4
# # - x=2; y=4-> 1
# # - x=-34; y=-30 -> 3

# def quarter(x, y):
#     if x > 0 and y > 0:
#         print('Это первая четверть')
#     elif x < 0 and y > 0:
#         print('Это вторая четверть')
#     elif x < 0 and y < 0:
#         print('Это третья четверть')
#     else:
#         print('Это четвертая четверть')
#     input()

# X = input("ввеедите x = ")
# Y = input("ввеедите y = ")
# quarter(X, Y)

# # Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# def func(x):
#     if x == 1:
#         print('x > 0 and y > 0')
#     elif x == 2:
#         print('x < 0 and y > 0')
#     elif x == 3:
#         print('x < 0 and y < 0')
#     elif x == 4:
#         print('x > 0 and y < 0')
#     input()

# X = input("ввеедите x = ")
# func(X)



# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,10
# - A (7,-5); B (1,-1) -> 7,21

a = []
b = []

a.append(int(input()))
a.append(int(input()))
b.append(int(input()))
b.append(int(input()))

print(((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5)