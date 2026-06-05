# def fibonacci(n: int):
#     if n < 0:
#         return -1
#     elif n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:    
#         prev2, prev1 = 0, 1
#         for i in range(0, n-1):
#             current = prev2 + prev1
#             prev2, prev1 = prev1, current
#             print('iterating once')
#             print(current, prev2, prev1)

#         return prev1

# sequence = {}
# for i in range(21):
#     sequence[i] = fibonacci(i)

# print(sequence)

def fibonacci(n: int):
    if n < 0:
        return -1
    else:    
        sequence = [0 , 1]
        for i in range(0, n-1):
            sequence.append(sequence[-1]+sequence[-2])
        return sequence[n]           

sequence = {}
for i in range(21):
    sequence[i] = fibonacci(i)

print(sequence)
