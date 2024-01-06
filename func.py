def win(row: list):
    if len(set(row)) == 1:
        return True
    return False


def unpack_field(field):
    for row in field:
        print(*row)


def stroke(n: int, m: int, player, field: list):
    if isinstance(n, int) and isinstance(m, int):
        if n not in range(0, 2) and m not in range(0, 2):
            print("Нет такого индекса. Только от 0 до 2")
    else:
        print("Должо быть число")
    if field[n][m]:
        print("Здесь уже занято")
    if player not in ("x", "o"):
        print("Нет такого игрока")
    else:
        field[n][m] = player


def generate_rows(layout: list):
    vert1 = [layout[i][0] for i in range(0, 3)]
    vert2 = [layout[i][1] for i in range(0, 3)]
    vert3 = [layout[i][2] for i in range(0, 3)]

    horiz1 = [i for i in layout[0]]
    horiz2 = [i for i in layout[1]]
    horiz3 = [i for i in layout[2]]

    main_diagonal = []
    for i in range(0, 3):
        main_diagonal.append(layout[i][i])

    sub_diagonal = []
    for i in range(3):
        for j in range(3):
            if j == 3 - i - 1:
                sub_diagonal.append(layout[i][j])

    rows = [vert1, vert2, vert3, horiz1, horiz2, horiz3, main_diagonal, sub_diagonal]
    return rows

