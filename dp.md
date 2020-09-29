

# Dynamic Programming



### Kadane's Algorithm



**Example 1: Buy and Sell Stock (easy)**: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

- Say you have an array for which the *i*th element is the price of a given stock on day *i*.

- If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

```python
def maxProfit(self, prices: List[int]) -> int:
  maxCur = maxSoFar = 0
  for i in range(1, len(prices)):
    maxCur = max(0, maxCur + prices[i] - prices[i - 1])
    maxSoFar = max(maxCur, maxSoFar)
  return maxSoFar
```

This problem could be solved using some other more intuitive ways, but here I want to introduce the idea of difference array and Kadane's algorithm.

```python
arr = [7, 1, 5, 3, 6, 4]
diff = [0, -6, 4, -2, 3, -2]
```

The idea of difference array is every simple. For i in range(1, len(arr) - 1), we compute arr[i] - arr[i - 1] and store the result at diff[i]. We set diff[0] as 0 by default.

Since we get the difference array, we need to prove that **the sum of the max sum subarray of the difference array** is the max profit in this example.

Suppose arr[j] and arr[i] (j > i) are any two points that give us the max difference (i.e. arr[j] - arr[i]). Then in our diff arr:

- diff[i + 1] = arr[i + 1] - arr[i]
- diff[i + 2] = arr[i + 2] - arr[i + 1] 
- diff[i + 3] = arr[i + 3] - arr[i + 2]
- ...
- diff[j] = arr[j] - arr[j - 1]

If we sum up diff[i + 1] to diff[j], we get exactly arr[j] - arr[i], thus we prove the difference between arr[j] - arr[i] is the sum of its difference array from index i + 1 to j. Since arr[j] - arr[i] has the max difference, we have to let the sum of diff arr be maximized, which is exactly the maximum sum arrary of the diff arr.

Ok, back to the problem, in order to find the maximum subarray of the difference array, we introduce Kadane's algorithm, which is a simple dynamic programming practice that could help us find maximum subarray in linear time.

The idea is very simple:

_For every element in the array, we are trying to find the maximum sum that each element could reach. The maximum sum is either the maximum sum previous elements combined + this element, or this element itself. (If we have to pick an element) or 0 (If we don't have to pick an element and the max sum of  previous subarray is negative)_

Here is the further explanation of this algorithm:  https://www.youtube.com/watch?v=86CQq3pKSUw&t=520s&ab_channel=CSDojo)



In this example, we store the maximum sum of the previous differences + current diff to maxCur. maxSoFar is storing the previous maximum sum without current diff (maximum subarray until i - 1). By summing up the difference and excluding the subarrary that sums to 0, we get the maximum subarray until i or 0 if there is no subarray that has a positive sum. Then we either take maximum subarray until i - 1 or maximum subarray until i by comparing these maxSoFar and maxCur.  This is the case where we have to get a positive integer or else we don't buy the stock, and it's like finding the maximum positive area in a continuous region under a curve.



Here is another leetcode problem, which is exactly to find the max sum subarray:

Example 1.2: Maximum Subarray (Easy): https://leetcode.com/problems/maximum-subarray/

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return *its sum*.

```python
def maxSubArray(nums: List[int]) -> int:
    max_cur = nums[0]
    for i in range(1, len(nums)):
        nums[i] = max(nums[i-1] + nums[i], nums[i])
        max_cur = max(nums[i], max_cur)
    return max_cur

# Or just:
def maxSubArray(nums: List[int]) -> int:
  """Find the largest sum of any contiguous subarray."""
  best_sum = current_sum = float('-inf')
  for x in nums:
    current_sum = max(x, current_sum + x)
    best_sum = max(best_sum, current_sum)
  return best_sum
```

This also uses the Kadane's algorithm. Basically, we just store the previous sum at nums[i - 1] in previous step and try to maximize nums[i] by taking max(nums[i - 1] + nums[i], nums[i])



The second approach is similar to Example one. However, since in this case we are asked to get a subarray with at least size 1, current_sum is set to max(x, current_sum + x) instead of max(0, current_sum + x).

