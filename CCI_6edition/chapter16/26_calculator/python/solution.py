

class Calculator:


    def digitForChar(self, char):
        if char == '0': return 0
        if char == '1': return 1
        if char == '2': return 2
        if char == '3': return 3
        if char == '4': return 4
        if char == '5': return 5
        if char == '6': return 6
        if char == '7': return 7
        if char == '8': return 8
        if char == '9': return 9
        raise Exception('Char is not a digit')

    def nextNum(self):
        if not self.hasNext():
            raise Exception('Expected number.')

        if not self.expression[self.location] in '0123456789.':
            raise Exception('Expected digit or period.')

        periodIndex = self.location if self.expression[self.location] == '.' else -1
        start = self.location
        end = start+1

        while end < len(self.expression) and self.expression[end] in '0123456789.':
            if self.expression[end] == '.':
                if 0 <= periodIndex:
                    raise Exception('Number has too many periods.')
                periodIndex = end
            end += 1

        if start == (end-1) and periodIndex == start:
            raise Exception('Number has no digits.')

        num = 0
        if 0 <= periodIndex:
            for digitIndex in range(start, periodIndex):
                num = 10 * num + self.digitForChar(self.expression[digitIndex])
            tenthPower = 10
            for digitIndex in range(periodIndex+1, end):
                digit = self.digitForChar(self.expression[digitIndex])
                num = num + digit / tenthPower
                tenthPower *= 10
        else:
            for digitIndex in range(start, end):
                num = 10 * num + self.digitForChar(self.expression[digitIndex])
        self.location = end
        return num


    def nextOperator(self):
        operator = self.next()
        if not operator in '/*+-':
            raise Exception('Expected operator')
        self.move()
        return operator

    def hasNext(self):
        while self.location < len(self.expression) and self.next().isspace():
            self.move()
        return self.location < len(self.expression)

    def next(self):
        return self.expression[self.location]

    def move(self):
        self.location += 1

    def calculate(self, expression):
        self.expression = expression
        self.location = 0

        if not self.hasNext():
            return None

        operatorStack, numberStack = [], []
        numberStack.append(self.nextNum())

        # print(operatorStack)
        # print(numberStack)
        # print(self.location)
        # print()

        while self.hasNext():
            operator = self.nextOperator()
            number1 = self.nextNum()

            # print(operatorStack)
            # print(numberStack)
            # print(self.location)
            # print()

            if operator in '+-':
                operatorStack.append(operator)
                numberStack.append(number1)
            else:
                number0 = numberStack.pop()
                if operator == '*':
                    numberStack.append(number0 * number1)
                else:
                    numberStack.append(number0 / number1)

        print(operatorStack)
        print(numberStack)
        print(self.location)
        print()

        result = numberStack[0]
        for i in range(len(operatorStack)):
            operator = operatorStack[i]
            numberRight = numberStack[i+1]
            if operator == '+':
                result = result + numberRight
            else:
                result = result - numberRight

        return result


calc = Calculator()

testcases = [
    ('2 * 3 + 5 / 6 * 3 + 15', 23.5),
    ('2*3+5/6*3+15', 23.5),
    ('1            +           1', 2),
    ('1', 1),
    ('         1', 1),
    ('1      ', 1),
    ('     1      ', 1),
    ('1.', 1),
    ('.1', .1),
    ('1.1', 1.1),
    ('1+1+1+1+1', 5),
    ('1-1-1-1-1', -3),
    ('3*3*3+1*3*3*3', 54),
    ('3*0', 0),
    ('0*3', 0),
    ('0*0', 0),
    ('1*0', 0),
    ('0*1', 0),
    ('1*1', 1),
    ('1000*.001', 1),
    ('3+4+5', 12),
    ('3+4*5', 23),
    ('3+4/5', 3.8),
    ('3*4+5', 17),
    ('3*4*5', 60),
    ('3*4/5', 2.4),
    ('3/4+5', 5.75),
    ('3/4*5', 3.75),
    ('3/4/5', .15),
    ('3+4-5', 2),
    ('3-4+5', 4),
    ('3-4-5', -6),
    ('3-4*5', -17),
    ('3-4/5', 2.2),
    ('3*4-5', 7),
    ('3/4-5', -4.25),
    # ERROR Cases
    # ('.1 + .1 + .1', .3), # Edge case that can't be handled
    # ('1.1.', 0),
    # ('.1.1', 0),
]

for expression, answer in testcases:
    print('EXPRESSION: "%s"' % (expression))
    print('ANSWER: %s' % (answer))
    solution = calc.calculate(expression)
    print('SOLUTION: %s' % (solution))
    assert(answer == solution)
    print()
