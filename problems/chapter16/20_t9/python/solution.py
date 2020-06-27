

def wordToT9Str(word):
    t9 = ''
    for char in word:
        if char == 'a' or char == 'b' or char == 'c':
            t9 += '2'
        elif char == 'd' or char == 'e' or char == 'f':
            t9 += '3'
        elif char == 'g' or char == 'h' or char == 'i':
            t9 += '4'
        elif char == 'j' or char == 'k' or char == 'l':
            t9 += '5'
        elif char == 'm' or char == 'n' or char == 'o':
            t9 += '6'
        elif char == 'p' or char == 'q' or char == 'r' or char == 's':
            t9 += '7'
        elif char == 't' or char == 'u' or char == 'v':
            t9 += '8'
        elif char == 'w' or char == 'x' or char == 'y' or char == 'z':
            t9 += '9'
        else:
            return None
    return t9


class T9Map:

    def __init__(self):
        self.lists = {}

    def add(self, key, value):
        if key in self.lists:
            self.lists[key].append(value)
        else:
            self.lists[key] = [value]

    def get(self, key):
        if key in self.lists:
            return self.lists[key]
        return None



# Preparation
lines = open('../words.txt', 'r')
words = T9Map()

for line in lines:
    word = line[0:-1] # Trim newline
    t9Value = wordToT9Str(word)
    if t9Value == None:
        continue

    words.add(t9Value, word)



# Testcases

for num in range(10000):
    solution = words.get(str(num))
    if solution != None:
        print(num, solution)


