#!/usr/local/bin/python3



def divingBoard(K):
    def recurse(k, freq, boards):
        if k == 0:
            print(' '.join(boards))
            return
        for key, value in freq.items():
            if value <= 0:
                continue
            freq[key] -= 1
            boards.append(key)
            recurse(k - 1, freq, boards)
            boards.pop()
            freq[key] += 1
    
    freq = {'longer': K, 'shorter': K}
    recurse(K, freq, [])


for i in range(10):
    print(i)
    divingBoard(i)
    print()