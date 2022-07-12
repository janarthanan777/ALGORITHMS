import math
import InsertionSort
def bucket(list):
    numberOfBucket = round(math.sqrt(len(list)))
    maxValue = max(list)
    arr = []
    for i in range(numberOfBucket):
        arr.append([])
    for j in list:
        index = math.ceil(j*numberOfBucket/maxValue)
        arr[index - 1].append(j)
    for k in range(numberOfBucket):
        arr[k] = InsertionSort.InsertionSort(arr[k])
    k = 0
    for i in range(numberOfBucket):
        for j in range(len(arr[i])):
            list[k] = arr[i][j]
            k = k + 1
    return list
l = [6, 1, 8, 2, 4, 7, 3, 5, 9]
print(bucket(l))