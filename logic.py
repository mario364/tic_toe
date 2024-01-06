# Игра "Крестики-нолики"
# Поле игры - матрица! 3x3
from func import *

field = [
    [None, None, None],
    [None, None, None],
    [None, None, None]
]
n, m = 3, 3

# Собираем в список все возможные выигрыши
# Нам нужны вертикали, диагонали и горизонтали

# Вертикали
vert1 = [field[0][0], field[1][0], field[2][0]]
vert2 = [field[0][1], field[1][1], field[2][1]]
vert3 = [field[0][2], field[1][2], field[2][2]]

# Горизонтали
horiz1 = field[0]
horiz2 = field[1]
horiz3 = field[2]

# Диагонали
# Элементы главной диагонали (с правого нижнего угла до левого верхнего угла) находятся с равными индексами
main_diagonal = []
for i in range(0, n):
    main_diagonal.append(field[i][i])

# Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1)
# где n — размерность матрицы, находятся на побочной диагонали.
sub_diagonal = []
for i in range(n):
    for j in range(m):
        if j == n - i - 1:
            sub_diagonal.append(field[i][j])

flag = True

rows = [vert1, vert2, vert3, horiz1, horiz2, horiz3, main_diagonal, sub_diagonal]

unpack_field(field)
while flag:
    n = input("Введите координату(от 0 до 2): ")
    m = input("Введите координату(от 0 до 2): ")
    player = input("Введите значок игрока(x или o): ")
    stroke(n, m, player, field)
    unpack_field(field)
    for row in rows:
        res = win(row)
        if not res:
            flag = False
