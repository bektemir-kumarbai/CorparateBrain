import random

def cocktail_sort(arr: list) -> list:
    n = len(arr)
    left = 0
    right = n - 1
    pointer = right

    while left < right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                pointer = i
        right = pointer

        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                pointer = i
        left = pointer
    
    return arr

lst: list = random.sample(range(1, 100), 10)
res = cocktail_sort(lst)
print(res)