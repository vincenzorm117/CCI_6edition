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



# def towers_of_hanoi(N):
# 	T = (list(range(N,0,-1)),[],[])
# 	def toh(n, src, buff, dst):
# 		if n == 0: 
# 			return
# 		toh(n-1, src, dst, buff)
# 		print(T)
# 		T[dst].append(T[src].pop())
# 		toh(n-1, buff, src, dst)
	
# 	toh(N, 0, 1, 2)
# 	print(T)



# def towers_of_hanoi2(N):
# 	T = (list(range(N,0,-1)),[],[])
# 	q = [(N, 0, 1, 2)]
# 	while 0 < len(q):
# 		n, src, dst, buff = q.pop()
# 		if n == 0: 
# 			continue
# 		q.append((n-1, src, dst, buff))
# 		T[dst].append(T[src].pop())
# 		q.append((n-1, buff, src, dst))



# towers_of_hanoi(3)

