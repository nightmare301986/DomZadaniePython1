'''Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является 
ли этот день выходным.
Пример:
- 6 -> да
- 7 -> да
- 1 -> нет'''

day_of_week = int(input("Введите № дня недели (порядковый номер от 1 до 7) > ")) #Ввод дня недели в виде цифры от 1 до 7
match day_of_week: #оператор выбора
    case 1: print("Понедельник. Рабочий день")
    case 2: print("Вторник. Рабочий день")
    case 3: print("Среда. Рабочий день")
    case 4: print("Четверг. Рабочий день")
    case 5: print("Пятница. Рабочий день")
    case 6: print("Суббота. Выходной день")
    case 7: print("Воскресенье. Выходной день")
    case _: print("Введите корректное значение (от 1 до 7)")