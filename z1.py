#1. Напишите функцию для транспонирования матрицы
def matrix(list_: list[list]) -> list[list]:
    return list(map(list, zip(*list_)))
print(matrix([[3, 2, 1], [6, 7, 8]]))