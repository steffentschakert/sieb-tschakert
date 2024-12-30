import numpy as np

# Ein einfaches Sudoku-Rätsel (0 steht für leere Felder)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(board, row, col, num):
    # Überprüfen der Zeile
    if num in board[row]:
        return False
    
    # Überprüfen der Spalte
    if num in [board[i][col] for i in range(9)]:
        return False
    
    # Überprüfen des 3x3-Quadrats
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Hauptprogramm
print("Willkommen zum Sudoku-Spiel!")
print("Hier ist das aktuelle Sudoku-Rätsel:")
print_board(sudoku_board)

while True:
    row = int(input("Geben Sie die Zeile (0-8) ein (oder -1 zum Beenden): "))
    if row == -1:
        break
    col = int(input("Geben Sie die Spalte (0-8) ein: "))
    num = int(input("Geben Sie die Zahl (1-9) ein: "))

    if is_valid(sudoku_board, row, col, num):
        sudoku_board[row][col] = num
        print("Aktualisierte Sudoku-Tafel:")
        print_board(sudoku_board)
    else:
        print("Ungültiger Zug, versuchen Sie es erneut.")

# Lösen des Sudoku-Rätsels
if solve_sudoku(sudoku_board):
    print("Das Sudoku wurde erfolgreich gelöst:")
    print_board(sudoku_board)
else:
    print("Das Sudoku hat keine Lösung.")