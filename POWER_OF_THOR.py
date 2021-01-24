'''
POWER OF THOR
Difficulty : Easy
題目來源：https://www.codingame.com/ide/puzzle/power-of-thor
'''
import sys
import math

# Solve this puzzle by writing the shortest code.
# Whitespaces (spaces, new lines, tabs...) are counted in the total amount of chars.
# These comments should be burnt after reading!

# lx: the X position of the light of power
# ly: the Y position of the light of power
# tx: Thor's starting X position
# ty: Thor's starting Y position
lx, ly, tx, ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The level of Thor's remaining energy, representing the number of moves he can still make.

    # 燈與索爾的X距離
    diffX = lx - tx
    # 燈與索爾的Y距離
    diffY = ly - ty

    # 情況1: 索爾在燈的位置 => 終止程式
    if diffX == 0 and diffY == 0:

        break

    # 情況2: 索爾和燈在同一條y軸 => 移動x軸即可
    elif abs(diffX) > 0 and diffY == 0:

        print("E" if diffX >= 0 else "W")

        tx = tx + 1 if diffX > 0 else tx - 1
    
    # 情況3: 索爾和燈在同一條x軸 => 移動y軸即可
    elif  abs(diffY) > 0 and diffX == 0:

        print("S" if diffY >= 0 else "N")

        ty = ty + 1 if diffY > 0 else ty - 1


    elif diffX > 0:

        # 情況4: 索爾在燈的左上角 => 往SE移動
        if diffY > 0:

            print("SE"); tx = tx + 1; ty = ty + 1

        # 情況5: 索爾在燈的左下角 => 往NE移動
        else:

            print("NE"); tx = tx + 1; ty = ty - 1

    elif diffX < 0:

        # 情況6: 索爾在燈的右上角 => 往SW移動
        if diffY > 0:

            print("SW"); tx = tx - 1; ty = ty + 1

        # 情況7: 索爾在燈的右下角 => 往NW移動
        else:

            print("NW"); tx = tx - 1; ty = ty - 1