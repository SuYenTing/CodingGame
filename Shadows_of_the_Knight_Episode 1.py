'''
Shadows of the Knight - Episode 1
Difficulty : Medium
題目來源：https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]

# maximum number of turns before game over.
n = int(input())

# 蝙蝠俠起始位置
x0, y0 = [int(i) for i in input().split()]

# 炸彈可能值域範圍
wMax = w
wMin = 0
hMax = h
hMin = 0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # 處理蝙蝠俠本回合跳躍目標x軸
    if "R" in bomb_dir:
        xTarget = x0 + math.ceil((wMax - x0)/2)
        wMin = x0 + 1  # 因為炸彈在右邊 所以左半部不可能有炸彈 縮小炸彈範圍

    elif "L" in bomb_dir:
        xTarget = x0 - math.ceil((x0 - wMin)/2)
        wMax = x0 - 1  # 因為炸彈在左邊 所以右半部不可能有炸彈 縮小炸彈範圍
    
    else:
        xTarget = x0

    # 處理蝙蝠俠本回合跳躍目標y軸
    if "U" in bomb_dir:
        yTarget = y0 - math.ceil((y0 - hMin)/2)
        hMax = y0 - 1  # 因為炸彈在上面 所以下半部不可能有炸彈 縮小炸彈範圍

    elif "D" in bomb_dir:
        yTarget = y0 + math.ceil((hMax - y0)/2)
        hMin = y0 + 1  # 因為炸彈在下面 所以上半部不可能有炸彈 縮小炸彈範圍

    else:
        yTarget = y0

    # the location of the next window Batman should jump to.
    print(str(xTarget) + " " + str(yTarget))

    # 更新蝙蝠俠位置
    x0 = xTarget
    y0 = yTarget