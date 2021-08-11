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

This solution applies the idea of couting sort (bucket sort) we learned in sorting chapter. First, we find the number with the most digit. Then, we create buckets with size of maxWidth + 1, storing every length of every digit.

Then, we visit every element el in arr, let res += el * len(arr) first because el would be used as the right-most digits for every digit combination (including itself). Then, we need to visit our buckets to map the number with corresponding number of digits



For example, arr = [2, 33, 105], the total string sum is 22 + 3333 + 105105 + 332 + 1052 + 10533 + 33105 + 233 + 2105

- 2 is used the length(3) times as right most, so does 33 and 105

- The maxWidth is 3, so we create buckets with size 4 (index 0 is not used by convention)

- Each bucket:

  - 1 : 1
  - 2 : 1
  - 3 : 1

- Which means a number is used on top of another number with bucket's number of time

- For instance, 2 is used as 200 in 233, 2000 in 2105, so we need to multiply 2 by 100 and 1000 for these two cases, which is 2 * buckets[i] * 10 ** i for any i

  

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

**Analysis:**

- We first sort all the intervals for simplicity
- Put the first interval to result
- When we need to add a new interval, there are two cases to consider:
  - if the new interval has starting time less than the ending time of the last interval in result, we then compare its ending time with the ending time of the last interval in result and take the max, this could help us form the new interval in overlapping case
  
  - if not overlapping, simply put the new interval into result
  
    

**Example 3: Non-overlapping Intervals (medium):** https://leetcode.com/problems/non-overlapping-intervals/

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key = lambda x: x[1])
    i = 1
    end = intervals[0][1]
    res = 0
    while i < len(intervals):
        if intervals[i][0] < end:
            res += 1
        else:
            end = intervals[i][1]
        i += 1
    return res
```
**Analysis:**

- This is the typical interval scheduling problem. In order to maximize the number of intervals, the idea is simple:
  - Always pick the interval that ends the earliest or starts the latest
- This problem could also be put into the greedy section but leave it here with the previous question makes more sense.



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

Since the condition is set, what we need to do is to always pick the two heaviest stones and smash them together

Since heap in python is min-heap, we'll use the negative-sign trick to implement a max-heap. Basically, we create a copy with all numbers negative, and heapify the negative version, and always pick the top two

For instance, [1,3,2,4], 4 3 2 1 would be the sequence (-4 -3 -2 -1), and you will first pick the largest, 4 and 3, minus them and put back the negative version, so 4 - 3 = -3 - 4



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

**Analysis:**

- The idea is simple - we do a two pass algorithm and keep track of the product in each pass
- In the first pass, we only consider the prod on the left, with i starting from index 1, the prod on the left are added to res[i], and prod is updated by multiplying nums[i]
- Then, we need to consider the prod on the right using the same idea





**Example 5: Queue Reconstruction by Height (medium):** https://leetcode.com/problems/queue-reconstruction-by-height/

You are given an array of people, `people`, which are the attributes of some people in a queue (not necessarily in order). Each `people[i] = [hi, ki]` represents the `ith` person of height `hi` with **exactly** `ki` other people in front who have a height greater than or equal to `hi`.

Reconstruct and return *the queue that is represented by the input array* `people`. The returned queue should be formatted as an array `queue`, where `queue[j] = [hj, kj]` is the attributes of the `jth` person in the queue (`queue[0]` is the person at the front of the queue).

```python
def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
    people.sort(key = lambda x: (-x[0], x[1]))
    res = []
    for p in people:
        res.insert(p[1], p)
    return res
```
**Analysis:**

- You sort the people based first on the height and then how many people should stay in front
- After that, we know that tallest people don't need to care about other people in front of them, and shortest people need to take into account every other people (assume people are unique)
- Then, we can insert the person based on k



**Example 6: Car Pooling (medium):** https://leetcode.com/problems/car-pooling/

You are driving a vehicle that has `capacity` empty seats initially available for passengers. The vehicle **only** drives east (ie. it **cannot** turn around and drive west.)

Given a list of `trips`, `trip[i] = [num_passengers, start_location, end_location]` contains information about the `i`-th trip: the number of passengers that must be picked up, and the locations to pick them up and drop them off. The locations are given as the number of kilometers due east from your vehicle's initial location.

Return `true` if and only if it is possible to pick up and drop off all passengers for all the given trips. 

```python
def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
    lst = []
    for n, start, end in trips:
        lst.append((start, n))
        lst.append((end, -n))
    lst.sort()
    pas = 0
    for loc in lst:
        pas += loc[1]
        if pas > capacity:
            return False
    return True
```
**Analysis:**

- For this problem, it's normal to think of it as an interval problem
- However, if you change your mind for one sec, you notice that it could be converted to an accumulation problem
- At any point, if the passengers accumulated over the capacity, we returns false
- Otherwise, we should return true
- Remember to sort the trips so that we can count properly