def insertionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1, len(list)):
            if list[min] > list[j]:
                min = j
        list[i], list[min] = list[min], list[i]
    return list
l = [2, 5, 9, 3, 1, 6, 7]
print(insertionSort(l))