

# Same as the missingNumber function but it can access the whole item from the array
#  instead of having to use the fetch function.
def realMissingNumber(array):
    N = len(array)
    nSum = N*(N+1)/2
    return int(nSum - sum(array))


# Fetch function described in problem
def fetch(array, i, j):
    return (array[i] >> j) & 1

# Calculate solution
def missingNumber(array):
    # Set of all the indeces of the array. We will remove half of the indeces in
    #  each loop iteration.
    indeces = set(range(len(array)))
    # Used to construct the missing value from the array.
    missingNumberValue = 0
    # For 0b0000100, the 1 corresponds to a value of j=2
    j = 0
    # Loop through all indeces until its empty. We will remove half
    #  of the indeces on each loop.
    while len(indeces) > 0:
        # Used to keep track of the ones and zeros found on the jth bit for the
        #  remaining values corresponding to the indeces in the indeces set.
        ones, zeros = 0, 0
        # Loop through the indeces and count the ones and zeros found in the
        #  jth bit of each element.
        for i in indeces:
            if fetch(array, i, j) == 1:
                ones += 1
            else:
                zeros += 1
        # Update missingNumberValue and set fetchValueForItemToKeep for the value of the jth bit
        #  for the items that we want to keep.
        if ones < zeros:
            missingNumberValue = missingNumberValue | (1 << j)
            fetchValueForItemToKeep = 1
        else:
            fetchValueForItemToKeep = 0
        # Remove half of the items from the set to narrow down the search.
        indeces = set(filter(lambda i : fetch(array, i, j) == fetchValueForItemToKeep, indeces))
        # Increment j
        j += 1
    # Return
    return missingNumberValue

# Loop through all possible N
for N in range(2, 10000):
    print(N)
    # Loop through all possible i that can be removed from 0...N
    for i in range(N+1):
        # Create complete list of 0...N
        array = list(range(N+1))
        # Create new list from previous, excluding i
        array = array[0:i] + array[i+1:N]
        # Find the missing number and compare with actual solution
        assert(missingNumber(array) == i)