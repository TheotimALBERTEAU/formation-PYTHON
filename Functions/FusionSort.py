def FusionSort(liste: list) -> list:
    if len(liste) <= 1:
        return liste

    middle = len(liste) // 2

    sublist1 = liste[:middle]
    sublist2 = liste[middle:]

    left_sorted = FusionSort(sublist1)
    right_sorted = FusionSort(sublist2)

    final_list = []
    i = 0
    j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            final_list.append(left_sorted[i])
            i += 1
        else:
            final_list.append(right_sorted[j])
            j += 1

    final_list.extend(left_sorted[i:])
    final_list.extend(right_sorted[j:])

    return final_list