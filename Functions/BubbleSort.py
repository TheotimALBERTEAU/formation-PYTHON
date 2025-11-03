def BubbleSort(list : list):
    sorted = False
    while not sorted:
        passes = 0
        for i in range(len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                passes += 1
        if passes == 0:
            sorted = True

    return list