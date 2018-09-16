#!/usr/local/bin/python3


T = 6

def printNPairsOfParentheses(N):
    nPairsOfParens = [['']]
    s = set()
    for i in range(1,N+1):
        s.clear()
        for option in nPairsOfParens[i-1]:
            s.add('('+option+')')
            s.add('()'+option)
            s.add(option+'()')
        nPairsOfParens.append(list(s))
    return nPairsOfParens
        

options = printNPairsOfParentheses(T)
# for i in range(len(options)):
#     print(i, '|', len(options[i]))
#     for s in options[i]:
#         print(s)


def addParen(ls, leftRem, rightRem, s, index):
    if leftRem < 0 or rightRem < leftRem: 
        return

    if leftRem == 0 and rightRem == 0:
        ls.append(''.join(s))
    else:
        s[index] = '('
        addParen(ls, leftRem - 1, rightRem, s, index+1)

        s[index] = ')'
        addParen(ls, leftRem, rightRem - 1, s, index+1)

def generateParens(count):
    s = list(' '*(count*2))
    l = list()
    addParen(l, count, count, s, 0)
    return l

for i in range(T):
    sol = generateParens(i)
    print(len(options[i]), len(sol))
    print(sol)

(((()))), ((()())), ((())()), ((()))(), (()(())), (()()()), (()())(), (())(()), (())()(), ()((())), ()(()()), ()(())(), ()()(()), ()()()(),