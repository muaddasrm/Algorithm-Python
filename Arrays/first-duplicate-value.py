def firstDuplicateValue(array):
    # Write your code here.
    memory=[]
    for i in array:
        if i in memory:
            return i
        memory.append(i)
    return -1