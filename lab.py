import PySimpleGUI as sg
from func import win, generate_rows
player = "X" 

layout = [
    [sg.Button("Пусто", size=(4, 4)), sg.Button("Пусто", key=1, size=(4, 4)), sg.Button("Пусто", key=2, size=(4, 4)), sg.Text(f"Ход {player}", size=(5, 4), key="player")],
    [sg.Button("Пусто", key=3, size=(4, 4)), sg.Button("Пусто", key=4, size=(4, 4)), sg.Button("Пусто", key=5, size=(4, 4))],
    [sg.Button("Пусто", key=6, size=(4, 4)), sg.Button("Пусто", key=7, size=(4, 4)), sg.Button("Пусто", key=8, size=(4, 4))],
    [sg.Text("Играем в крестики-нолики!", key="text", size=(15, 10))]
]

window = sg.Window("Крестики-нолики", layout, size=(250, 300))
cnt = 0

while True:
    event, values = window.read()
    print(window[event])
    if event == sg.WIN_CLOSED:
        break
    if event or event == 0:
        if window[event].ButtonText == "Пусто":
            cnt += 1
            if event in range(0, 3):
                layout[0][event] = player
                window[event].update(player)
                print(layout[0])
            if event in range(3, 6):
                layout[1][event - 3] = player
                window[event].update(player)
                print(layout[1])
            if event in range(6, 9):
                layout[2][event - 6] = player
                window[event].update(player)
                print(layout[2])
            player = 'O' if player == 'X' else 'X'
            window["player"].update(f"Ход {player}")



    rows = generate_rows(layout)
    for row in rows:
        res = win(row)
        if res:
            window["text"].update(f"Победили {row[0]}!")
        if not res and cnt == 9:
            window["text"].update("Ничья!")
