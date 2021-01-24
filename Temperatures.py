'''
Temperatures
Difficulty : Easy
題目來源：https://www.codingame.com/ide/puzzle/the-descent
'''
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

if n == 0:
    print(n)
else:
    numList = list()
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        numList.append(t)
    minValue = min([abs(elem) for elem in numList])
    print(max([elem for elem in numList if abs(elem) == minValue]))