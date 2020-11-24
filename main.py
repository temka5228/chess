import math

ChessBoard = [[0] * 8 for i in range(0, 8)]
mas_let = ["k", "l", "m", "n"]
mas_dot = [0, 0, 0, 0]
One_Color = False
Threat_Queen = False
Threat_Bishop = False
for i in range(0, 8):
    for j in range(0, 8):
        if (i + j) % 2 == 0:
            ChessBoard[i][j] = '###'
        else:
            ChessBoard[i][j] = '___'


def Display_Chessboard():
    print('    ________________________')
    for i in range(0, 8):
        print(8 - i, ' |', end='')
        for j in range(0, 8):
            print(ChessBoard[7 - i][j], end='')
        print('|', sep='\n', end='\n')
    print('    ͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞͞')
    print('     a  b  c  d  e  f  g  h')


def Input_Number():
    global k, l, m, n
    for i in range(len(mas_dot)):
        while True:
            try:
                print('Введите ', mas_let[i], ': ', end='')
                mas_dot[i] = int(input()) - 1
                if -1 < mas_dot[i] < 8:
                    break
            except BaseException:
                pass
    k, l, m, n = mas_dot[0], mas_dot[1], mas_dot[2], mas_dot[3]


def Check_Color():
    global One_Color
    if (l + k) % 2 == (n + m) % 2:
        print('a) Клетки одного цвета')
        One_Color = True
    else:
        print('a) Клетки разного цвета')
        One_Color = False


def Check_Ferz():
    global Threat_Queen
    if l == n or k == m:
        print('б) Ферзь угрожает')
        Threat_Queen = True
    elif ((k > m and l > n) or (k < m and l < n)) and k - l == m - n:
        print('б) Ферзь угрожает')
        Threat_Queen = True
    elif ((k > m and l < n) or (k < m and l > n)) and k + l == m + n:
        print('б) Ферзь угрожает')
        Threat_Queen = True
    else:
        print('б) Ферзь не угрожает')


def Check_Knight():
    if k + l + 3 == m + n or k - l - 3 == m - n or k + l - 3 == m + n or k - l + 3 == m - n:
        if (k + 2 == m and l + 1 == n) or (k + 2 == m and l - 1 == n) or (k + 1 == m and l + 2 == n) or (
                k + 1 == m and l - 2 == n) or \
                (k - 2 == m and l + 1 == n) or (k - 2 == m and l - 1 == n) or (k - 1 == m and l + 2 == n) or (
                k - 1 == m and l - 2 == n):
            print('в) Конь угрожает')
    else:
        print('в) Конь не угрожает')


def Check_Rook():
    if k == m or l == n:
        print('г) С поля', k + 1, l + 1, 'можно попасть в поле', m + 1, n + 1, 'за один ход')
    else:
        print('г) С поля', k + 1, l + 1, 'можно попасть в поле', m + 1, n + 1, 'за два хода.')
        print('Промежуточный ход на координаты', k + 1, n + 1, 'или на координаты', m + 1, l + 1)


def Check_Bishop():
    global One_Color
    print("е) ", end='')
    if One_Color == True:
        for i in range(0, len(ChessBoard)):
            for j in range(0, len(ChessBoard)):
                i1 = 7 - i
                x1, y1, x2, y2 = k - j, l - i1, m - j, n - i1
                cos = x1 * x2 + y1 * y2
                try:
                    ug = round(math.degrees(math.acos((x1 * 1) / ((x1 * x1 + y1 * y1) ** (0.5)))), 5)
                    if cos == 0 and (ug == 45 or ug == 135):
                        if j == m and i1 == n:
                            print('   Возможен ход слоном в один ход')
                        else:
                            print('   Возможный промежуточный ход слоном на поле:', j + 1, i1 + 1)
                except BaseException:
                    pass
    else:
        print('С поля', k + 1, l + 1, 'на поле', m + 1, n + 1, 'слоном попасть нельзя')


def Check_Ferz_Motion():
    global Threat_Queen
    print("д) ", end='')
    if Threat_Queen == True:
        print("Ферзем можно сходить за один ход")
    else:
        for i in range(0, len(ChessBoard)):
            for j in range(0, len(ChessBoard)):
                i1 = 7 - i
                x1, y1, x2, y2 = k - j, l - i1, m - j, n - i1
                try:
                    ug = round(math.degrees(math.acos((x1 * 1) / ((x1 * x1 + y1 * y1) ** (0.5)))), 5)
                    ug1 = round(
                        math.degrees(
                            math.acos((x1 * x2 + y1 * y2) / (((x1 ** 2 + y1 ** 2) * (x2 ** 2 + y2 ** 2)) ** (0.5)))), 5)
                    if (ug1 == 90 or ug1 == 45 or ug1 == 135) and (
                            ug == 45 or ug == 135 or ug == 0 or ug == 90 or ug == 180):
                        print('   Возможный промежуточный ход ферзем на поле:', j + 1, i1 + 1)
                except BaseException:
                    pass


if __name__ == '__main__':
    Input_Number()
    ChessBoard[l][k] = ' 1 '
    ChessBoard[n][m] = ' 2 '
    Display_Chessboard()
    Check_Color()
    Check_Ferz()
    Check_Knight()
    Check_Rook()
    Check_Ferz_Motion()
    Check_Bishop()
