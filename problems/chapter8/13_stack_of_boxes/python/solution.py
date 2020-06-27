#!/usr/local/bin/python3

# def compare_boxes(self,b):
#     w_a, h_a, d_a = self
#     w_b, h_b, d_b = b
#     if w_a == w_b:
#         if h_a == h_b:
#             if d_a == d_b: return 0
#             else: return d_a - d_b
#         else: 
#             return h_a - h_b
#     else:
#         return w_a - w_b

def compare_boxes(a,b):
    return a[0] > b[0] and a[1] > b[1] and a[2] > b[2]


def stack_of_boxes2(boxes):
    # Sort boxes
    boxes.sort(reverse=True)
    memoize = [0] * len(boxes)
    # Recurse
    def recurse(boxes, boxIndex, memoize):
        boxMaxHeight = boxes[boxIndex][1]
        for i in range(boxIndex+1, len(boxes)):
            nextBoxMaxHeight = boxes[i][1]
            # Get the max height of the next box
            if 0 < memoize[i]:
                nextBoxMaxHeight = memoize[i]
            else:
                nextBoxMaxHeight = recurse(boxes, i, memoize)
            
            if compare_boxes(boxes[boxIndex], boxes[i]):
                boxMaxHeight = max(boxMaxHeight, boxes[boxIndex][1] + nextBoxMaxHeight)
            else:
                boxMaxHeight = max(boxMaxHeight, nextBoxMaxHeight)
        memoize[boxIndex] = boxMaxHeight
        return boxMaxHeight

    boxMaxHeight = 0
    for i in range(len(boxes)):
        boxMaxHeight = max(boxMaxHeight, recurse(boxes, i, memoize))
    return boxMaxHeight

    
def stack_of_boxes3(boxes):
    def recurse(boxes, boxIndex):
        maxHeight = 0
        for i in range(boxIndex+1, len(boxes)):
            if compare_boxes(boxes[boxIndex], boxes[i]):
                maxHeight = max(maxHeight, recurse(boxes, i))
        maxHeight += boxes[boxIndex][1]
        return maxHeight

    boxes.sort(reverse=True)
    maxHeight = 0
    for i in range(len(boxes)):
        maxHeight = max(maxHeight, recurse(boxes, i))
    return maxHeight

   
def stack_of_boxes4_final(boxes):
    def recurse(boxes, boxIndex, memoize):
        maxHeight = 0
        for i in range(boxIndex+1, len(boxes)):
            if compare_boxes(boxes[boxIndex], boxes[i]):
                if 0 < memoize[i]:
                    maxHeight = max(maxHeight, memoize[i])
                else:
                    maxHeight = max(maxHeight, recurse(boxes, i, memoize))
        maxHeight += boxes[boxIndex][1]
        memoize[boxIndex] = maxHeight
        return maxHeight

    boxes.sort(reverse=True)
    memoize = [0] * len(boxes)
    maxHeight = 0
    for i in range(len(boxes)):
        maxHeight = max(maxHeight, recurse(boxes, i, memoize))
    return maxHeight

    
    

def stack_of_boxes(boxes):
    def sob(unused, used, topBox, heightMax, stackHeight):
        if len(unused) == 0:
            return sum([h[1] for h in used])
        if topBox == None:
            for box in unused:
                # Move box from unused to used
                unused.remove(box)
                used.add(box)
                # Recurse
                heightMax = sob(unused, used, box, heightMax, stackHeight + box[1])
                # Move box back to unused category
                unused.add(box)
                used.remove(box)
        else:
            topWidth, topHeight, topDepth = topBox
            for box in unused:
                width, height, depth = box
                m = heightMax
                if width < topWidth and height < topHeight and depth < topDepth:
                    # Move box from unused to used
                    unused.remove(box)
                    used.add(box)
                    # Recurse
                    heightMax = sob(unused, used, box, heightMax, stackHeight + box[1])
                    # Move box back to unused category
                    unused.add(box)
                    used.remove(box)
        return max(heightMax, stackHeight)

    if not isinstance(boxes, list):
        return 0
    if len(boxes) <= 0:
        return 0
    return sob(set(boxes), set(), None, 0, 0)



testcases = [
    [
        (41,59,61),
        (79,34,43),
        (90,49,69),
        (54,28,47),
        (31,75,34)
    ],
    [
        (0,0,0),
        (1,1,1),
        (2,2,2),
        (3,3,3),
        (4,4,4),
    ],
    [
        (0,0,0),
        (1,1,1),
        (2,2,2),
        (3,3,0),
        (4,4,4),
    ],
    [
        (39,94,16),
        (9,77,80),
        (99,11,86),
        (94,77,57),
        (7,58,15)
    ],
    [
        (59,40,16),
        (26,19,74),
        (61,18,45)
    ]
]

for boxes in testcases:
    print(boxes)
    print(stack_of_boxes(boxes))
    print(stack_of_boxes2(boxes))
    print(stack_of_boxes3(boxes))
    print(stack_of_boxes4_final(boxes))