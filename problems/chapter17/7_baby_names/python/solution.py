

########################################
# Helpers

class BabyNode:
    def __init__(self, name, freq):
        self.name = name
        self.freq = freq
        self.synonyms = []


########################################
# Solutions

def baby_names(names, synonyms):
    babyNodes = {}
    for name, freq in names:
        babyNodes[name] = BabyNode(name, freq)

    for name0, name1 in synonyms:
        if name0 in babyNodes and name1 in babyNodes:
            babyNodes[name0].synonyms.append(name1)
            babyNodes[name1].synonyms.append(name0)

    visited = set()
    for startName in babyNodes:
        if startName in visited:
            continue
        # Perform DFS from current node to visit all nodes connected to curr nodee
        freq = 0
        stack = [startName]
        while len(stack) > 0:
            name = stack.pop()
            visited.add(name)
            freq += babyNodes[name].freq
            for synonym in babyNodes[name].synonyms:
                if synonym in visited:
                    continue
                stack.append(synonym)
        print(startName, freq)




########################################
# Testcases


testcases = [
    (
        [
            ('John', 15),
            ('Jon', 12),
            ('Chris', 13),
            ('Kris', 4),
            ('Christopher', 19),
        ],
        [
            ('Jon', 'John'),
            ('John', 'Johnny'),
            ('Chris', 'Kris'),
            ('Chris', 'Christopher'),
        ],
    ),
]

for names, synonyms in testcases:
    baby_names(names, synonyms)