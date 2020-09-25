from heapq import heappop, heappush
arr = [5, 3, 2, 1, 21, 8, 4, 3, 20, 10, 2, 1, 233, 2341]


def heapsort(arr):
    heap = []
    for val in arr:
        heappush(heap, val)
    arr[:] = [heappop(heap) for i in range(len(heap))]


def bubble_sort(arr):
    n = len(arr)
    while True:
        swapped = False
        for i in range(1, len(arr)):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        i += 1


def merge(a, aux, lo, mid, hi):
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            aux[k] = a[j]
            j += 1
        elif j > hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1


def merge_sort(arr, aux, lo, hi):
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    merge_sort(aux, arr, lo, mid)
    merge_sort(aux, arr, mid + 1, hi)

    merge(arr, aux, lo, mid, hi)
    if arr[mid + 1] > arr[mid]:
        return


def m_sort(arr):
    aux = arr[:]
    merge_sort(aux, arr, 0, len(arr) - 1)


def merge_2(arr, aux, lo, mid, hi):
    aux = arr[:]
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            arr[k] = aux[j]
            j += 1
        elif j > hi:
            arr[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            arr[k] = aux[j]
            j += 1
        else:
            arr[k] = aux[i]
            i += 1


def t_d_mergesort(arr):
    n = len(arr)
    aux = arr[:]
    sz = 1
    while sz < n:
        lo = 0
        while lo < n - sz:
            merge_2(arr, aux, lo, lo + sz - 1, min(lo + (sz << 1) - 1, n - 1))
            lo += (sz << 1)
        sz <<= 1

def counting_sort(arr):
    min_el = min(arr)
    range_arr = max(arr) - min_el + 1
    buckets = [0 for _ in range(range_arr)]
    result = []
    
    for val in arr:
        buckets[val - min_el] += 1
        
    for i, v in enumerate(buckets):
      	while v > 0:
            result.append(i + min_el)
            v -= 1
    arr[:] = result

def radix_sort(arr):
    
# bubble_sort(arr)
# insertion_sort(arr)
# t_d_mergesort(arr)
#test = [5,2,6]
# m_sort(arr)
# t_d_mergesort(test)
print(arr)
counting_sort(arr)
print(arr)
# print(test)
# print(arr)
