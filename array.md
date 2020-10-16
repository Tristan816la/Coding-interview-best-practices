# Array



**Example 1: String sum (medium) (Adapted from mock coding interview question)**

- Given an array of string arr, given two index i and j (i could be equal to j), return the sum of string representation of arr[i] + arr[j]
- For instance, assume arr = [2, 10], arr[0] ''+'' arr[0] = 22, arr[0] "+" arr[1] = 210, arr[1] "+" arr[0] = 102, arr[1] "+" arr[1] = 1010, so the result should be 1010 + 102 + 210 + 22 = 1344

Time exceeded Brute-force solution (O(n^2)):

```python
def stringsum2(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            res += int(str(arr[i]) + str(arr[j]))
    return res
```

**Real solution** (O(nk), k is the length of the number with max digits):

```python
def stringsum(arr):
    maxWidth = 0
    res = 0

    for i in arr:
        if len(str(i)) > maxWidth:
            maxWidth = len(str(i))

    buckets = [0 for i in range(maxWidth + 1)]

    for i in arr:
        buckets[len(str(i))] += 1

    for el in arr:
        res += el * len(arr)
        for i in range(1, len(buckets)):
            res += el * buckets[i] * 10 ** i
    return res
```

**Analysis:**

This solution applies the idea of couting sort (bucket sort) we learned in sorting chapter. First, we find the number with the most digit. Then, we create buckets with size of maxWidth + 1, storing every 



**Example 2: Merge Intervals (medium):** https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

**Solution:**

```python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort()
    result = [intervals[0]]
    i = 1
    while i < len(intervals):
        if intervals[i][0] <= result[-1][1]:
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])
        i += 1
    return result
```



**Example 3: Last Stone Weight (Easy):** https://leetcode.com/problems/last-stone-weight/

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two **heaviest** stones and smash them together. Suppose the stones have weights `x` and `y` with `x <= y`. The result of this smash is:

- If `x == y`, both stones are totally destroyed;
- If `x != y`, the stone of weight `x` is totally destroyed, and the stone of weight `y` has new weight `y-x`.

At the end, there is at most 1 stone left. Return the weight of this stone (or 0 if there are no stones left.)

**Solution:** 

```python
from heapq import heapify, heappush, heappop

def lastStoneWeight(self, stones: List[int]) -> int:
    stonecp = [-s for s in stones]
    heapify(stonecp)
    while len(stonecp) > 1:
        l1 = -heappop(stonecp)
        l2 = -heappop(stonecp)
        heappush(stonecp, l2 - l1)

    return -stonecp[0]
```
**Analysis:**



**Example 4: Product of Array Except Self (medium):** https://leetcode.com/problems/product-of-array-except-self/

Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Solution:** 

```python
def productExceptSelf(self, nums: List[int]) -> List[int]:
    res = [1] * len(nums)
    prod = nums[0]
    for i in range(1, len(nums)):
        res[i] = prod
        prod *= nums[i]
        
    prod = nums[-1]
    
    for j in range(len(nums) - 2, -1, -1):
        res[j] *= prod
        prod *= nums[j]
        
    return res
```