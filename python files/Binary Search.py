def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

li_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(li_numbers, 7))


def binary_search(search_list, value):
    path_to_target = []
    low = 0
    high = len(search_list) - 1
    while low <= high:
        mid = (low + high) // 2
        value_at_middle = search_list[mid]
        path_to_target.append(value_at_middle)

        if value == value_at_middle:
            return (path_to_target, f'Value found at index {mid}')
        elif value > value_at_middle:
            low = mid + 1
        else:
            high = mid - 1

    return [], "Value not found"

#print(binary_search([1, 2, 3, 4, 5], 3))
#print(binary_search([1, 3, 5, 9, 14, 22], 10))


print(binary_search([1, 2, 3, 4, 5, 9], 4))

"""
0 <= 5 Ok
    m = 2
    vm = 3
    3
    4 == 3 no
    4 > 3 ok
        l = 2+1 =3
3 <= 5 ok
    m = 4
    5
    4==5 no
    4 > 5 no    
    h = 3

3 <= 3 ok 
    m = 3
    4
    4 == 4 ok
    yes 3
   

(3,5,4)
"""