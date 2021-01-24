'''
The Descent
Difficulty : Easy
題目來源：https://www.codingame.com/ide/puzzle/the-descent
'''
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.

# game loop
while True:

    # 最大高度起始值
    maxHeight = 0
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        
        # 若當前的山高度比最大高度還要高 則更新資訊
        if mountain_h > maxHeight:
            maxHeight = mountain_h
            targetMountain = i

    # The index of the mountain to fire on.
    print(targetMountain)
