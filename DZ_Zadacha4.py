'''Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
Пример:
- A (3,6); B (2,1) -> 5,09
- A (7,-5); B (1,-1) -> 7,21'''

x1 = int(input('Введите x1 ')) #Приглашение ко вводу координат
y1 = int(input('Введите y1 '))
x2 = int(input('Введите x1 '))
y2 = int(input('Введите y1 '))

dlina = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))**0.5 #Формула определения расстояния между точками

print('Длина отрезка в 2D пространстве составляет: ' , f'{dlina:.3f}')