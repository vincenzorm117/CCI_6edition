#!/usr/local/bin/python3


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
    ]
]

for boxes in testcases:
    print(boxes)
    print(stack_of_boxes(boxes))