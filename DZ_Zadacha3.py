'''Напишите программу, которая по заданному номеру четверти, 
показывает диапазон возможных координат точек в этой четверти (x и y).'''

quarter = int(input('Введите номер четверти: ')) #Приглашение ко вводу номера четверти

match quarter: #Условия определения значений принадлежащих плоскостям
    case 1: print("Диапазон значений x > 0, y >0")
    case 2: print("Диапазон значений x < 0, y >0")
    case 3: print("Диапазон значений x < 0, y <0")
    case 4: print("Диапазон значений x > 0, y <0")
    case _: print("Введите подходящее значение для номера четверти от 1 до 4")
