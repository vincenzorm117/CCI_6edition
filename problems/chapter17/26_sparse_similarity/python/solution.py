

def computeSimilarity(doc1, doc2):
    if len(doc1.intersection(doc2)) > 0:
        return len(doc1.intersection(doc2)) / len(doc1.union(doc2))
    return 0


def solution_brute_force(docs):
    for i in range(len(docs)):
        for j in range(i+1, len(docs)):
            similarity = computeSimilarity(docs[i][1], docs[j][1])
            if 0 < similarity:
                print(docs[i][0], docs[j][0], similarity)


def solution_optimized(docs):
    # Build dictionary of doc id to the array length of its letters
    docToLetterCount = {}
    for docId, letters in docs:
        docToLetterCount[docId] = len(letters)
    # Build dictionary of letters to list of documents
    letterToDocs = {}
    for docId, letters in docs:
        for letter in letters:
            if letter in letterToDocs:
                letterToDocs[letter].append(docId)
            else:
                letterToDocs[letter] = [docId]

    docTupleHashToTuple = {}
    docTupleToIntersectionSize = {}

    # Iterate through each letter and docs
    for letter in letterToDocs:
        # Loop through all non-directional doc ordered pairs
        docs = letterToDocs[letter]
        for i in range(len(docs)):
            for j in range(i+1, len(docs)):
                # Generate doc tuple based on the doc id order
                if docs[i] < docs[j]:
                    docTuple = (docs[i], docs[j])
                else:
                    docTuple = (docs[j], docs[i])
                # Save tuple from hash for use later
                docTupleHashToTuple[hash(docTuple)] = docTuple
                # Update edge weight between two docs
                if hash(docTuple) in docTupleToIntersectionSize:
                    docTupleToIntersectionSize[hash(docTuple)] += 1
                else:
                    docTupleToIntersectionSize[hash(docTuple)] = 1
    # Loop through all pairs of documents that have similarity greater than 0
    for key in docTupleToIntersectionSize:
        # Pull the two documents
        doc1, doc2 = docTupleHashToTuple[key]
        # Get document pair intersection size
        I = docTupleToIntersectionSize[key]
        # Calculate similarity: I / U = I / (A + B - I) where A + B are the sizes of the documents.
        similarity = I / (docToLetterCount[doc1] + docToLetterCount[doc2] - I)
        print(doc1, doc2, similarity)



testcases = [
    [
        (13, set([14, 15, 100, 9, 3])),
        (16, set([32, 1, 9, 3, 5])),
        (19, set([15, 29, 2, 6, 8, 7])),
        (24, set([7, 10])),
    ]
]

for docs in testcases:
    print('Brute Force')
    solution_brute_force(docs)
    print('Optimized')
    solution_optimized(docs)