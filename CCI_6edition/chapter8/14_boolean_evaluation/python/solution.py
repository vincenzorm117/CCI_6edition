#!/usr/local/bin/python3

def parse_boolean(expression):
    values, operators = [], []
    for char in expression:
        if char == '1':
            values.append(1)
        elif char == '0':
            values.append(0)
        elif char == '&':
            operators.append(0)
        elif char == '|':
            operators.append(1)
        elif char == '^':
            operators.append(2)
    return (values, operators)
    

def num_boolean_evaluations(expression, answer):
    values, operators = parse_boolean(expression)

    def recurse(start, end, values, operators):
        if start == end:
            if values[start] == 1:
                return (0,1)
            else:
                return (1,0)
        ones, zeros = 0, 0
        for i in range(start, end):
            leftZeros, leftOnes = recurse(start, i, values, operators)
            rightZeros, rightOnes = recurse(i+1, end, values, operators)
            if operators[i] == 0: # & AND
                zeros += leftOnes * rightZeros + leftZeros * rightZeros + leftZeros * rightOnes
                ones += leftOnes * rightOnes
            elif operators[i] == 1: # | OR
                zeros += leftZeros * rightZeros
                ones += leftOnes * rightOnes + leftOnes * rightZeros + leftZeros * rightOnes
            elif operators[i] == 2: # ^ XOR
                zeros += leftZeros * rightZeros + leftOnes * rightOnes
                ones += leftZeros * rightOnes + leftOnes * rightZeros
            else:
                raise ValueError('Invalid operator')
        return (zeros, ones)
            
    zeros, ones = recurse(0, len(values)-1, values, operators)
    if answer:
        return ones
    else:
        return zeros



testcases = [
    ("1^0|0|1", False),
    ("0&0&0&1^1|0", True)
]


for expression, answer in testcases:
    print('Case: %s %s' % (expression, answer))
    print(num_boolean_evaluations(expression, answer))