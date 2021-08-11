# Sliding Window Approach

Sliding window is a commonly used approach to slide over the given data to capture the portion with the desired characteristics.

An example of this type of problem is to find the max subarray with size k.

For this problem, the brute force approach lists all possible continuous subarrary and get their max, which is O(n^2). However, using a window that drops the first element every time, we can find the max using O(n) time.

The key for this type of problem is to find the best way to **_slide_** the window.

**How to identify Sliding Window Problem:**

1. Iterable items

- **_Contiguous_** sequence of elements
- Strings, arrays, linked lists

2. min, max, longer, shorter, contained

**Common Patterns:**

1. Type 1: Window with fixed size
2. Type 2: Dynamic size window
3. Type 3: Dynamic size window with auxilary data structures
4. Type 4: Fixed size window with auxilary data structures

**Corresponding Problems**

- Type 1 & Type 2:
  Type 1 and type 2 are just warm-up problems. I haven't found them on Leetcode, but they could be helpful to lay the foundation to understand the sliding window problems

1. Find the max subarray with size k (easy)

```python
def findMaxSubarray(arr, k):
    maxVal = -float("inf")
    curSum = 0
    for i in range(len(arr)):
        curSum += arr[i]
        if i >= k - 1:
            maxVal = max(maxVal, curSum)
            curSum -= arr[i - k + 1]
    return maxVal

```

2. Smallest Subarray With Given Sum (medium)

- Given an arrry and a target, find the size of the smallest subarray that sums to the target

```python
def smallestSubarr(arr, target):
    minSize = float("inf")
    curSum = 0
    start = 0
    for i in range(len(arr)):
        curSum += arr[i]
        while(curSum >= target):
            minSize = min(minSize, i - start + 1)
            curSum -= arr[start]
            start += 1
    return minSize
```

Analysis:
In this example, we traverse the entire arr using i, and at the moment we find the curSum is larger than or equal to the target, we increase start by one and see if curSum could still suffice the condition (i.e. curSum >= target). We get the size of window by calculating i - start + 1. We keep track of the smallest size of the subarray by using a variable minSize.

Example: Minimum Size Subarray Sum:

- Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

```python
def minSubArrayLen(s: int, nums: List[int]) -> int:
    if not nums:
        return 0
    result = float("inf")
    curSum = 0
    start = 0
    for i in range(len(nums)):
        curSum += nums[i]
        while curSum >= s:
            result = min(i - start + 1, result)
            curSum -= nums[start]
            start += 1

    if result == float("inf"):
        result = 0

return result
```

Type 3: Longest Substring Without Repeating Characters (medium)

- Given a string s, find the length of the longest substring without repeating characters.

**_Solution:_**

```python
def lengthOfLongestSubstring(s: str) -> int:
    res = 0
    hashmap = collections.defaultdict(int)
    left = right = 0
    while right < len(s):
        if s[right] in hashmap:
            left = max(left, hashmap[s[right]] + 1)
        res = max(right - left + 1, res)
        hashmap[s[right]] = right
        right += 1
    return res
```

- Analysis:
  In order to find the longest substring with unique characters, what we can do here is to keep a dynamic size window with an auxilary hashmap. The hashmap could help us keep track of the index of the **last occurance** of the character. And if we visit a repeating character, we simply only need to update the left pointer to the index of the last occurance of this repeating character if the left pointer is smaller than the index of the last occurance.

  We also use the max trick to maintain the largest res.

Type 4:
Find all anagrams in a string (medium)

- Given a string s and a non-empty string p, find all the start indices of p's anagrams in s. 
  <ins>Definition of anagram:</ins> An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

**_Solution_**

```python
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pCounter = [0 for _ in range(26)]
        sCounter = [0 for _ in range(26)]
        res = []
        a = ord('a')

        for char in p:
            pCounter[ord(char) - a] += 1

        k = len(p)

        for i in range(len(s) - k + 1):
            if i > 0:
                sCounter[ord(s[i - 1]) - a] -= 1
                sCounter[ord(s[i + k - 1]) - a] += 1
            else:
                for j in range(k):
                    sCounter[ord(s[j]) - a] += 1

            if sCounter == pCounter:
                res.append(i)

        return res
```

- Analysis:
  In the naive approach, I simply called isAnagram(substr, p) to every single substring, which would take O(n^2) time since I listed alll possible substrings and the comparison would also at most take O(n^2). This was the point that I realized that I didn't have a mastery of this topic, so in the following analysis, I would walk through the optimization I did to reduce the time complexity to O(n).
  
  To determine if two strings are anagrams, there usually are two methods:

1. Sort two strings and see if their sorted versions are the same: O(nlogn)
2. Use **_Counting Sort_**: O(n)

   - Counting sort is a sorting technique based on keys between a specific range. It works by counting the number of objects having distinct key values (kind of hashing). Then doing some arithmetic to calculate the position of each object in the output sequence. (From https://www.geeksforgeeks.org/counting-sort/)

   In this example, we first creates the counter for both S and P. Then, we "hash" all elements of P into the counter. Next, we loop through S by maintaining a window size k = len(P). In the first window, we add all the elements to the counter, but in the subsequent slides of window, we simply only need to drop the previous first character in the counter and add new last character to the counter. At last, we check if sCounter is the same as pCounter to tell if S and P are anogram. (We don't actually need to sort S and P using counting sort to identify if they are anagrams)

   A huge optimization I have done is to ignore the characters in the middle of the window. As they were in the counter previouse step (i.e. i > 0), I simply don't need to care about them. This is the same idea of the example in the introduction.

Type 3 challenging: Minimum Window Substring (Hard)
-   Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

```python
    def minWindow(self, s: str, t: str) -> str:
        def valid(counter):
            for v in counter.values():
                if v > 0:
                    return False
            return True
        
        tCounter = collections.Counter(t)
        start = 0
        result = ""
        minSize = float("inf")
        
        for r in range(len(s)):
            if s[r] in tCounter:
                tCounter[s[r]] -= 1
            while valid(tCounter):
                if minSize > r - start + 1:
                    result = s[start : r + 1]
                    minSize = len(result)
                
                if s[start] in tCounter:
                    tCounter[s[start]] += 1
                    
                start += 1
                
        return result
```
Even though this is a hard problem on leetcode, it applies the same idea we had before -- a dynamic size window with a counter to check if the substring is valid.

Basically, we maintained a counter containing the count of each element of t. When we reach the point that a substring contains all the char in t, we increase the start by one until the substring is invalid again.



Extra Example: Subarray Sum Equals K (medium): https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers and an integer **k**, you need to find the total number of continuous subarrays whose sum equals to **k**.

```python
def subarraySum(self, nums: List[int], k: int) -> int:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    
    sumCounter = collections.Counter()
    count = 0
    
    for num in nums:
        if num - k in sumCounter:
            count += sumCounter[num - k]
        if num == k:
            count += 1
        sumCounter[num] += 1
        
    return count
```
Analysis:

You might think to solve this problem using the sliding window approach. However, this problem ***cannot*** solve by sliding window (If you trick by this problem, star this repo plz). Why? Because if the sum is larger or smaller than k, it doesn't mean the window is too large or two small (But if we restrain this problem to sorted array or only positive number, we might use the sliding window approach)

Remember, when using the sliding window approach, you need to notice:

1. `If a wider scope of the sliding window is valid, the narrower scope of that wider scope is valid` must hold.
2. `If a narrower scope of the sliding window is invalid, the wider scope of that narrower scope is invalid` must hold.

(From: https://leetcode.com/problems/subarray-sum-equals-k/discuss/301242/General-summary-of-what-kind-of-problem-can-cannot-solved-by-Two-Pointers)



Let's go over the solution. For the above problem, we used a concept called prefix-sum array, which could be explained by the example below:

```
arr = [0, 1, 3, 5, 7]
prefix_sum = [0, 1, 4, 9, 16]
```

prefix_sum[0] = arr[0], prefix_sum[1] = arr[0] + arr[1], prefix_sum[2] = arr[0] + arr[1] + arr[2], and so on so forth.



If we know the prefix sum, what do we know about the subarray? Well, if we pick i = 1 and j = 3, we know sum(arr[i : j]) == prefix_sum[j] - prefix_sum[i - 1]. In the above arr, sum from arr[i] to arr[j] is 1 + 3 + 5 = 9. Prefix_sum[j] - prefix_sum[i - 1] is indeed arr[1] + arr[2] + ... + arr[j] - arr[1] - arr[2] - ... arr[i - 1], which is exactly 1 + 3 + 5.



How does this help our problem? Well, since we are trying to find how many subarrays sum to the target k, we can use this trick to get how many subarrays have the sum k. Normally, we need to use O(n^2) time to pick satisfying prefix_ sum[m]  and prefix_sum[n], however, does this remind you a familiar problem that basically everyone has seen on leetcode?



Yes. Two sum! 



We revised the two sum solution a little bit by using a counter. Since this time we are trying to find how many elements prefix_sum[n] before prefix_sum[m] such that prefix_sum[m]  - prefix_sum[n] = k. We also need to notice that the prefix_sum[m] itself can be equal to k, which is why we add another if statement for tackling this case.