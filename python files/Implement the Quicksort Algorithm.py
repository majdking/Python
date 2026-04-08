def quick_sort(list_ints) -> list:
    if len(list_ints) <= 1:
        return list_ints
    sorted_list = []
    pivot = list_ints[0]
    list_less = []
    list_equal = []
    list_great = []

    for e in list_ints:
        if not isinstance(e, int):
            raise ValueError('It should all the list is from integers')
        if e < pivot:
            print(e)
            list_less.append(e)
        elif e == pivot:
            print(e)
            list_equal.append(e)
        else:
            print(e)
            list_great.append(e) 

    list_less = quick_sort(list_less)
    list_great = quick_sort(list_great)

    sorted_list = list_less + list_equal + list_great

    return sorted_list

print(quick_sort([]))
print(quick_sort([20, 3, 14, 1, 5]))
print(quick_sort([83, 4, 24, 2]))
print(quick_sort([4, 42, 16, 23, 15, 8]))
print(quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56]))