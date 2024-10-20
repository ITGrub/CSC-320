
def bubbleSort(list):
    indexing_length = len(list) - 1
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(0, indexing_length):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
    return list
print ("The test scores in order are:")    
print(bubbleSort([2, 11, 98, 23, 48, 33, 97, 61, 3]))
