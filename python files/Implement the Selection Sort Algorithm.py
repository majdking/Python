def selection_sort(list_items) -> list:
    length = len(list_items)
    sort_index = 0
    while sort_index < length:
        selected_list = list_items[sort_index:]
        try:
            minimum_element = min(selected_list)
        except Exception:
            print("The list's elements must be integers")
            return
        minimum_element_index = selected_list.index(minimum_element)
        swapping_element = selected_list[sort_index - sort_index]
        if minimum_element == swapping_element:
            sort_index += 1
            continue
        list_items[sort_index] = minimum_element
        list_items[minimum_element_index + sort_index] = swapping_element
        #print(f'minimum element: {minimum_element} and his index: {minimum_element_index}\n swapping element: {swapping_element} and his index: {sort_index}')
        #print(list_items)
        sort_index += 1

    #print('done')
    return list_items 

print(selection_sort([33, 1, 89, 2, 67, 245]))         
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))
print(selection_sort([1,55,7,1,2,55]))
print(selection_sort([1,55,7,1,2,55,'2']))