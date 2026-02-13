import heapq

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

massive_data = [1000, 1, 50, 200, 3, 99, 10000]
print(heap_sort(massive_data))
