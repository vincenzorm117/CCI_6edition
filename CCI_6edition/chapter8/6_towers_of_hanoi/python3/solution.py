#!/usr/local/bin/python3

N = 3
towers = [[],[],[]]
for i in range(N,0,-1):
    towers[0].append(i)
    

def solve_hanoi(k, src, temp, dest):
    if k <= 0: return
    solve_hanoi(k-1,src,dest,temp)
    towers[dest].append(towers[src].pop())
    print(towers[0],towers[1],towers[2])
    solve_hanoi(k-1,temp,src,dest)


print(towers[0],towers[1],towers[2])
solve_hanoi(N, 0, 1, 2)
print(towers[0],towers[1],towers[2])



