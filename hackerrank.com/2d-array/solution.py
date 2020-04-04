#!/bin/python3

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


maxHourglass = -63
for i in range(4):
    for j in range(4):
        sum = arr[i][j] + arr[i+1][j] + arr[i+2][j] + arr[i+1][j+1] + arr[i][j+2] + arr[i+1][j+2] + arr[i+2][j+2]
        if maxHourglass <= sum:
            maxHourglass = sum

print(maxHourglass)


