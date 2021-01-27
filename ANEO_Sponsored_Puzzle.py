'''
ANEO Sponsored Puzzle
Difficulty : Medium
題目來源：https://www.codingame.com/ide/puzzle/aneo
備註：此解法最後只通過90% 且程式碼太過冗長 網路上有其他更好的思路可解
'''

import sys
import math

# 自定義函數 計算最適速度區間
def IntervalFunction(speed, distance, duration):
    
    # 在最大速限下需要的調整速度因子
    adjSpeedFactor = math.floor(distance / duration * 3.6 / speed)

    # 計算最適速度區間
    if  adjSpeedFactor == 0:
        minReqSpeed = distance / ((adjSpeedFactor+1) * duration) * 3.6
        maxReqSpeed = speed

    else: 
        if adjSpeedFactor % 2 != 0:
            adjSpeedFactor += 1
        minReqSpeed = distance / ((adjSpeedFactor+1) * duration) * 3.6
        maxReqSpeed = distance / (adjSpeedFactor * duration) * 3.6

    return([math.floor(minReqSpeed), math.floor(maxReqSpeed), adjSpeedFactor])


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
speed = int(input())         # 最大速度(km/h)
light_count = int(input())   # 紅綠燈數量

print("speed: " + str(speed), file=sys.stderr, flush=True)
print("light_count: " + str(light_count), file=sys.stderr, flush=True)

# 取出距離與號誌切換時間資料
distanceList = list()
durationList = list()
intervalSpeed = list()
for i in range(light_count):

    distance, duration = [int(j) for j in input().split()]
    # distance: 距離(meters)
    # duration: 號誌切換時間(seconds)
    distanceList.append(distance)
    durationList.append(duration)

    # 計算最適速度區間
    intervalSpeed.append(IntervalFunction(speed, distance, duration))

    # 印出訊息
    print("distance: " + str(distance), file=sys.stderr, flush=True)
    print("duration: " + str(duration), file=sys.stderr, flush=True)

print(intervalSpeed, file=sys.stderr, flush=True)

# 檢查各區段是否都能以最適速度區間的最高速通過
while True:

    # 各區間最高速的最低值做為答案
    minMaxSpeed = math.floor(min([elem[1] for elem in intervalSpeed]))
    print(minMaxSpeed, file=sys.stderr, flush=True)

    # 若最適速度答案不在各區間範圍內 則進行調整
    notMatchSite = [i for i, elem in enumerate(intervalSpeed) if not elem[1] >= minMaxSpeed > elem[0]]
    print(notMatchSite, file=sys.stderr, flush=True)

    # 若皆符合則跳離迴圈 不符合則進行調整
    if not notMatchSite:
        break

    else:
        for i in notMatchSite:
            intervalSpeed[i] = IntervalFunction(speed=minMaxSpeed, 
                                                distance = distanceList[i], 
                                                duration = durationList[i])

    print(intervalSpeed, file=sys.stderr, flush=True)


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(minMaxSpeed)


