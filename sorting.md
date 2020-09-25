# Sort

This document only shows the implementation of different type of sorting and something that worths noticing. The ideas of different sorting algorithms are commonly taught in data structure and algorithm courses.

I made a note on "never", "sometimes", "often" to show the frequencies of these sorting algorithms I've done on leetcode

## Easy sorting algorithms

### 1. Insertion sort: O(n^2) (never):

```python
def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
        i += 1
```

Insertion sort is really fast when there is only a few items in the arrary (better than quicksort).

### 2. Bubble sort: O(n^2) (never): 

Bubble sort is the least useful sort I could think of.

```python
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
```

## Must-known sorting algorithms

### 3. Extra space mergesort: O(nlogn) (sometimes)

```python
# Sort both halves of arr and store the result to aux
def merge(arr, aux, lo, mid, hi):
    i, j = lo, mid + 1
    for k in range(lo, hi + 1):
        # Notice roles are swapped, see example below for a not-swapped version
        if i > mid:
            aux[k] = arr[j]
            j += 1
        elif j > hi:
            aux[k] = arr[i]
            i += 1
        elif arr[j] < arr[i]:
            aux[k] = arr[j]
            j += 1
        else:
            aux[k] = arr[i]
            i += 1

def merge_sort(arr, aux, lo, hi):
    if hi <= lo: return
    mid = lo + (hi - lo) // 2

    # Both halves of arr are sorted
    merge_sort(aux, arr, lo, mid)
    merge_sort(aux, arr, mid + 1, hi)

    # merge two halves of arr and store the result into aux
    merge(arr, aux, lo, mid, hi)

     # Optimization 1: If we find the smallest element of the second half is larger than the largest element of the first half, we can stop merging because the arr is already sorted

     # Notice in the end aux is the array we want to sort, so we need to merge first and then stop at here
    if arr[mid + 1] > arr[mid]: return

def m_sort(arr):
    aux = arr[:]
    # Optimization 2: swap the roles of aux and arr
    # so we don't need to create aux in merge, which reduces time
    merge_sort(aux, arr, 0, len(arr) - 1)
```

Note: The swap of roles are a little bite difficult to understand. Please try to understand the actual meaning of each function (Hope my comment would be helpful). Otherwise, not swapping roles is also fine

(Bonus): _In-place mergesort_: O(nlogn)
From: https://www.geeksforgeeks.org/in-place-merge-sort/

- Top-down mergesort

```python
def merge(arr, start, mid, end):
     start2 = mid + 1;

     # If the direct merge is already sorted
     if (arr[mid] <= arr[start2]):
         return;

     # Two pointers to maintain start
     # of both arrays to merge
     while (start <= mid and start2 <= end):

         # If element 1 is in right place
         if (arr[start] <= arr[start2]):
             start += 1;
         else:
             value = arr[start2];
             index = start2;

             # Shift all the elements between element 1
             # element 2, right by 1.
             while (index != start):
                 arr[index] = arr[index - 1];
                 index -= 1;

             arr[start] = value;

             # Update all the pointers
             start += 1;
             mid += 1;
             start2 += 1;

 # l is for left index and r is right index of
 # the sub-array of arr to be sorted

 def mergeSort(arr, l, r):
     if (l < r):

     # Same as (l + r) / 2, but avoids overflow
     # for large l and r
     m = l + (r - l) // 2;

     # Sort first and second halves
     mergeSort(arr, l, m);
     mergeSort(arr, m + 1, r);

     merge(arr, l, m, r);
```

Top-down mergesort still requires O(logn) space as the recursion would use the call stack for O(logn) times

_Bottom-up mergesort:_ 
 (For array, this is not an in-place method, but for linked list, O(1) space is achievable)

```python

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

 def b_u_mergesort(arr):
     n = len(arr)
     aux = arr[:]
     sz = 1
     while sz < n:
         lo = 0
         while lo < n - sz:
             merge_2(arr, aux, lo, lo + sz - 1, min(lo + (sz * 2) - 1, n - 1))
             lo += (sz * 2)
         sz <<= 1
```

In this example, sz denotes the size of the half window of the elements to be merged. At first, we merge all elements in pairs. Then, we'll merge all elements with the window size 4 (sz = 2) and so on so forth. In the end, we would merge only two subarray, since everything is sorted, we simply need to comparing all elements in the two subarrays and sort them using merge() function.

Bottom-up approach requires O(n) space if we use the auxilary data structure, but it could be an inplace O(1) algorithm in the following linked list example.

Example: Sort List (medium)
Given the head of a linked list, return the list after sorting it in ascending order.

```python
def sortList(head: ListNode) -> ListNode:
    def merge(l1, l2):
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next



    if not head or not head.next:
        return head
    # 1. Find the middle node of the linked list
    fast, slow, prev = head, head, head

    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next

    # 2. Divide into two halves and sort each halves
    prev.next = None
    l1 = sortList(slow)
    l2 = sortList(head)

    # 3. Merge the two sorted lists
    return merge(l1, l2)

```

This implementation is indeed an top-down mergesort, but it requires extra space O(logn) since we used the recursion.

There is indeed a bottom-up solution for this problem

```python
def sortList(head):
    if not head or not head.next:
        return head

    def getSize(head):
        counter = 0
        while head:
            counter += 1
            head = head.next
        return counter

    # Split the linked list at step, and return a pointer to the first element of the second list
    def split(head, step):
        i = 1
        while i < step and head:
            head = head.next
            i += 1
        if not head: return None
        # Disconnect
        result, head.next = head.next, None
        return result

    # Merge the two sorted linked list l, r, return the tail of the merged list
    def merge(l, r, head):
        cur = head
        while (l and r):
            if l.val < r.val:
                cur.next, l = l, l.next
            else:
                cur.next, r = r, r.next
            cur = cur.next
        cur.next = l if l else r
        while cur.next: cur = cur.next
        return cur

    size = getSize(head)
    step = 1
    dummy = ListNode(0)
    dummy.next = head
    l, r, tail = None, None, None

    while step < size:
        cur = dummy.next
        tail = dummy
        # Tail of the previous merged list is the begining of the second sublist that needs to be merged
        while cur:
            l = cur
            r = split(l, bs)
            cur = split(r, bs)
            tail = merge(l, r, tail)
        step <<= 1
    return dummy.next
```

Since we are using a linked list, it is worth noticing that we just use constant space, which could suffice the O(1) space requirement of this question.

## 4. Quicksort

Quicksort is a sorting algorithm that is, namely, really fast. It is of O(nlogn) time but it is usually faster than mergesort. The implementation of quicksort requires a _partition_ function.

```python
def partition(arr, l, r):
    pivot = arr[r]
    i, j = l - 1, l
    while j < r:
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
        j += 1
    arr[r], arr[i + 1] = arr[i + 1], arr[r]
    return i + 1


def quicksort(arr, l, r):
    if l < r:
        p = partition(arr)
        quicksort(arr, l, p - 1)
        quicksort(arr, p + 1, r)
```

Similar to mergesort, quicksort is also a divide-and-conquer, and it is easily implemented by using recursion. First, we partition the arr and find the pivot, then we quicksort everything less than te pivot and everything greter than the piviot.

### **Explaination for the partition function:**
The partition function might look confusing at first. But if you understand the purpose and mechanism, this function becomes pretty easy to understand.

First, we pick a random pivot in the arr (in this case, in order easier implementation, we pick the rightmost element as pivot)

Then, we apply the two-pointer method. We are trying to divide the array into two regions: between 0 and i, everything is less than pivot, and between i and len(arr),
everything is greater or equal to the pivot.

In order to achieve the above goal, let's use the j = 0 pointer to traverse the entire arr and see what we can do. When arr[j] is greater than or equal to pivot, we don't need to update i since that's exactly what we want. However, when arr[j] is smaller than pivot, we need to include it to the region between 0 and i. So, we firstly increase i by 1, at this point we know arr[i] is larger than pivot. Then swap arr[i] with arr[j] so that arr[j] has an element that is larger than pivot, and arr[i] has an element that is smaller than the pivot.

In the end, after traversing the entire array except for the pivot, we know the pivot should be put at index i + 1 as every element 0 - i is smaller than pivot, every element between i - len(arr) - 1 is greater than pivot. So we swap arr[i + 1] with pivot and return the index of the pivot for quicksort future usages.

One key thing to notice is that after partitioning the arrary, pivot is sitting in the place that it should be sitting, as the definition of partition means every element that is less than pivot is placed at left, and every element that is larger than pivot is placed to the right. So, after ensuring the position of one element, we only need to quicksort the left and right part of this function.

## 5. Heapsort

In this section, I would use the python heapq library to implement the heapsort. Heapsort takes O(nlogn) time, and O(n) space since we create a heap (represented by an arrary) to store all the elements

This is the implementation from the heapq documentation: https://docs.python.org/2/library/heapq.html

```python
from heapq import heappop, heappush, heapify

def heapsort(arr):
    heap = []
    for val in arr:
        heappush(heap, val)
    arr[:] = [heappop(heap) for _ in range(len(heap))]
    
# Or just:
def heapsort_2(arr):
  	heapify(arr)
  	arr[:] = [heappop(arr) for _ in range(len(arr))]

```



For reference, heappop toke O(logn) time per element, heappush took O(logn) time per element, thus heapsort is an O(nlogn) algorithm.



# Non-comparison based sort

Due to the property of comparison based sort, examples above can only reach the O(nlogn) time complexity at most. The following implementations would shed some lights on the O(n) sorting algorithms that actually exists. But, they usually require extra spaces, like a lot extra.

## 6. Counting sort

```python
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
```

Time complexity: O(n + k), where k is the range of the arr.

Space complexity: O(n + k) (p.s. We can also do an inplace counting sort, so it could be done using O(k) space)



One disadvantage of counting sort is that if the range of arr is too large, let's say 1 to n^2, this algorithm would take O(n^2) time, which is slower than the comparison based sort. In order to solve this problem, let's introduce radix sort.

## 7. Radix sort

From: https://www.programiz.com/dsa/radix-sort

```python
# Using counting sort to sort the elements in the basis of significant places
def countingSort(array, place):
    size = len(array)
    output = [0] * size
    count = [0] * 10

    # Calculate count of elements
    for i in range(0, size):
        index = array[i] // place
        count[index % 10] += 1

    # Calculate cummulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Place the elements in sorted order
    i = size - 1
    while i >= 0:
        index = array[i] // place
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


# Main function to implement radix sort
def radixSort(array):
    # Get maximum element
    max_element = max(array)

    # Apply counting sort to sort elements based on place value.
    place = 1
    while max_element // place > 0:
        countingSort(array, place)
        place *= 10
```



## Summary



For reference of the time complexity of each different sorting algorithms, I did a problem on leetcode and got the following result.

Problem: sort an array: https://leetcode.com/problems/sort-an-array/



| Algorithms           | Time                            | Space   |
| -------------------- | :------------------------------ | ------- |
| Insertion sort       | Time limit exceeded             | \       |
| Bubble sort          | Time limit exceeded             | \       |
| Bottom-up merge sort | Time limit exceeded             | \       |
| Top-down merge sort  | 340 ms                          | 19.8 MB |
| Quicksort            | 308 ms                          | 19.6 MB |
| Counting sort        | 156 ms                          | 22.3 MB |
| Heapsort             | 152 ms                          | 20.3 MB |
| Python Built-in sort | 144 ms                          | 19.7 MB |
| Radix sort           | Not be able to handle negatives | \       |
|                      |                                 |         |

Bottom-up merge sort requires O(n) space so it causes huge overhead.