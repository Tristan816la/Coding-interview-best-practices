

# Dynamic Programming



### Description

We'll now begin our journey to dynmiac programming. In this section, we're going to find the difference between the dynamic programming and the greedy approach. In the real world, dynamic programming is commonly used when there are seemingly no obvious solutions to a certain problems. At this time, we need to enumerate all the possibiliaties in order to find the solution, and dynamic programming is just the approach to help us to do this.



For dynamic programming question, there are two things to keep in mind:

- Optimal Solution
- Recurrence Relation (Subproblems)



And there is one approach we need to use:

- Memoize



Also there are several constraints of DP, though it is really powerful:

(i)  There are only a polynomial number of subproblems.

(ii)  The solution to the original problem can be easily computed from the solutions to the subproblems. (For example, the original problem may actually *be* one of the subproblems.)

(iii)  There is a natural ordering on subproblems from“smallest”to“largest,” together with an easy-to-compute recurrence that allows one to determine the solution to a subproblem from the solutions to some number of smaller subproblems.



Below, I'll firstly show you some questions and then some leetcode examples so that you could fully understand when and where to utilize the magnificent dp approach.

### Question 1: Weighted Interval Scheduling

**Problem:** Given a set of weighted intervals, I1, I2, ..., Ik, each interval has a weight w1, w2, ..., wk, find the set of non-overlapping intervals that has the maximum sum of weights.

**Thought process:**

- In the non-weighted interval problem, we used the greedy approach. However, the greedy approach simply doesn't work for this example, as the interval that ends the latest doesn't have to have the biggest weight. So, we need to come up with another approach
- At this time, by trying the greedy paradigms a few times, you realize there is no solution to solve this problem simply, so what you can do is to come back to the brute-force approach and try to optimize it
- But there are still methods that in our original problem that might be useful: we could sort the ending time so that we can consider each case later



**Dynamic Programming Formulation:**

- We now need to enumerate all possibilities
- Assume after sorting the intervals we have S1 <= S2 <= S3 .... <= Sk
- We will also define a disjoint index dis(Si) for each interval i such that dis(Si) = Sm such that Sm is the last interval that come before Si and doesn't not overlap with Si
- Assume there is an optimal solution O
- For each interval Si, there are two subproblems:
  - Si in O: then all intervals between dis(Si) and Si should not included in the optimal solution
  - Si not in O: then the optimal set is equal to the optimal set we could find using the subsets S1, S2, ..., Si - 1



**Dynamic Programming Solution:**

- Assume sorted intervals S is an array consisting of weights with size n
- Initialize an array dp, define dp[0] = 0 as convention

- for i in range(1, n + 1):
  - dp[i] = max(S[i] + dp[dis(S)], dp[i - 1])



**Time Complexity Analysis**

- O(n) calls of recurrence relation (But in order to find dis(S), we might need to use O(n), depending on if dis(S) is given or not)



By exploring this problem, you can see the basic component dp is based: **a reccurence relation that expresses the optimal solution in terms of the optimal solutions to smaller subproblems**



### Question 2: Least Square Error (I.e. Line of the Best Fit)

**Problem:**

Suppose our data consists of a set *P* of *n* points in the plane, denoted (*x*1, *y*1), (*x*2, *y*2), . . . , (*xn*, *yn*); and suppose *x*1 < *x*2 < . . . < *xn*. Given a line *L* defined by the equation *y*=*ax*+*b*, we say that the *error* of *L* with respect to *P* is the sum of its squared “distances” to the points in *P*

A natural goal is then to find the line with minimum error; this turns out to have a nice closed-form solution that can be easily derived using calculus.

However, if we are allowed to use n lines, the solution becomes trivial as we could add lines to every point to reduce the error to zero

So, we need a problem formulation that requires us to fit the points well, using as few lines as possible. 

Thus, our question becomes: finding the min(errors + cL), where c is a constant and L is the total number of lines we use



**Thought Process:**

- Assume we denote each points as P1, P2, P3, .... in the nondecreasing order of x coordinates

- Suppose we let OPT(i) denote the optimum solution for the previous points P1, P2, ..., Pi (OPT(0) = 0)
- There are two subproblems
  - If the last segement of the optimal partition is Pi, ..., Pn, then the value of the optimal solution is OPT(n) = OPT(i - 1) + C + ei,n (C means the constant for adding a new line, ei,n means the error if we add a segment starting from Pi and ending at Pn)
  - In order to get the minimum error for each n when we iterate through dp, we need to make sure at any given n we consider all the cases (that is, i between 1 and n)



**Dynamic Programming Solution**

- Initialize an array dp with size n + 1

- for i in range(1, n + 1):
  - dp[i] = min(dp[i - 1] + C + ej, i for j in range(1, i))



**Time Complexity analysis**

- There are O(n^2) pairs of points, and in order to calculate the error between each pair,  we need to use an error formula that takes O(n), so the total runnign time to get all the errors are O(n^3)
- For our dp, both our i-loop and j-loop only takes O(n), so the algorithm takes O(n^2)



### Quetions 3: Knapsack Problem

**Problem:**

- We have a knapsack that can at most take n pounds of item
- Assuming we are also given a set of k items, each item has a value vi and weight wi
- Determine how we can take the maximum value of items



**Intuition:**

- First greedy doesn't work for this problem, since we cannot just take the item with the largest unit value, since we cannot cut an object. We have to take an entire object
- So, there is only one obvious solution: list all possibilities

- But we'll use DP to simplify our process. Notice that once we pick an item i, the maximum amount we can take become n - wi but our value increase by vi. If we don't take an item, then we can take n pounds of item from the rest of other item
  - We can take the max of the above to get the best value of either taking or not taking the item i, which is all two possibilities
- So, assume our dp(i, j) could answer the following question
  - Given first i items and a knapsack with capacity j, what's the max value it could take?

- Of course, for our base cases, when we don't have any item, the max value should be 0. When, we only have one item, the max value should be the value of this item if our knapsack can take it



**Algorithm:**

[I should use square brackets, but md prevents me to do so]

- Initialize a 2D array dp with size (k + 1) * (n + 1) to 0
- for(j = 1; j < dp[0]; j += 1):
  - if j > items[0]: dp(0, j) = items.val
- for (i = 1; i < dp; i += 1):
  - for (j = 1; j < dp[0]; j +=1):
    - dp(i, j) = max(dp(i - 1)(j - items[i].weight) + items[i].value, dp(i - 1)(j))
- return dp(k)(n)



**Time Complexity:**

- O(nk): since we essential create a dp table with size O(nk) and iterate through every entry and do a constant operation for each entry
- This is not a polynomial time algorithm, since k could be any number



**Example 1: Coin Change (medium):**  https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money *amount*. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an infinite number of each kind of coin.



### Question 4: RNA Sequence

- AUGC are the four bases of the RNA sequence
- Assume there is a sequence AAUUCAGAU
- We can do a pairing: A <-> U and C <-> G, however, we have a rule of matching
  - Only A <-> U and C <->G
  - Matching is one-to-one
  - no crossing: If (i, j) and (k, l) are two pairs in S, then we cannot have i < k < j < l
  - no sharp turns
    - e.g. when i is matched with j, i < j - 4 in the sequence
- What is the maximum number of matching we could have?



**Intuition**:

The trouble comes when we try writing down a recurrence that expresses OPT(*j*) in terms of the solutions to smaller subproblems. We can get partway there: in the optimal secondary structure on *b*1*b*2 . . . *b**j*, it’s the case that either

- .  *j* is not involved in a pair; or
- .  *j* pairs with *k* for some *k* < *j* − 4.

Also,  because of the noncrossing condition, if you picked to connect j with k, we now know that no pair can have one end between 1 and *k* − 1 and the other end between *k* + 1 and *j* − 1. 



**Algorithm:**

Let's just use the previous skills we have learnt in those previous questions

- Initialize dp(n + 1)(n + 1), where dp(i)(j) is to answer the question: what is the maximum number of base matching we can get from range i to j
- Initialize dp(*i*,*j*)=0 whenever *i*≥*j*−4
- for i in range(1, n):
  - for j in range(1, i)
    - dp(i)(j) =max(dp(i)(k - 1) + dp(k + 1)(j - 1) + 1, dp(i)(j - 1))  # for k in range(0, j - 4)
- return dp(1)(n)



### Question 5: Shortest Path

**Introduction:** 

- DP could also be used to find the shortest path in a weighted graph, and its complexity is pretty intersting compared to other algorithms like Dijkstra and Bellman Ford.



**Problem**:

- Just regular shortest path for weighted graph, we denote starting point as s and ending point as t, an edge {u, v} represents the edge between vertex u and v. But this problem allows the graph to have negative edges (but no negative cycle)



**Intuition:**

- We set a constraint on the number of edges we can use, let l = the number of edges we can use
- If the path uses at most i - 1 edges, then we can the optimal path using i edges is equal to the optimal path using i - 1 edges

- The idea is pretty simple, the shortest path from s to t is the minimum of the shortest path from s to t's neighbors plus the weight of the edge {nbr, t}.



**Algorithm:**

- ShortestPath(s, t):
  - n = number of nodes in G
  - Initialize dp[n, V]
  - Define dp[0, t] = 0 and dp[0, v] = INF for all other v in V
  - For i = 1 to n - 1:
    - For v in V in any order:
      - dp(i, v) = min(dp(i - 1, k) + Wvk) for k in V



**Example 1: Cheapeast Flight With K Stops (medium):** https://leetcode.com/problems/cheapest-flights-within-k-stops/

- There are `n` cities connected by `m` flights. Each flight starts from city `u` and arrives at `v` with a price `w`.

- Now given all the cities and flights, together with starting city `src` and the destination `dst`, your task is to find the cheapest price from `src` to `dst` with up to `k` stops. If there is no such route, output `-1`.

**Solution:**

```python
def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    # dp(i)(j) Answer the question the shortest path to reach point j using at most i edges
    # return dp[K][dst] in the end
    # K stop = K + 1 Edges
    dp = [[float("inf") for _ in range(n + 1)] for _ in range(K + 2)]
    
    # Dis to src is always zero
    for i in range(K + 2):
        dp[i][src] = 0
        
    for i in range(1, K + 2):
        for flight in flights:
            s, e, w = flight
            if dp[i - 1][s] != float("inf"):
                dp[i][e] = min(dp[i][e], dp[i - 1][s] + w)
                
    return dp[K + 1][dst] if dp[K + 1][dst] != float("inf") else -1
```
- This is the leetcode version of dp of minimum weighted path. Notice that in order to solve the problem, we firstly did a few things
  1. distance to src node is 0, no matter how many edges we use
  2. distance should be initialized to inf for every node at first
  3. The main for-loop only checks i from 1 to K + 1. Since it doesn't make sense to use 0 edge to reach any point 
     - (python implementation wouldn't tell that there is an error using dp[i-1] when there is an error)
  4. The recurrence relation is exactly the same, meaning that if there is an edge to any start point using i - 1 edge, there should be an edge to end point using i edges. so we just need to find the minimum by considering all the edges



### Question 6: Sequence Alignment, aka Longest Common Subsequence

**Problem:**

- Given two sequences, e.g., L: aabacad, S: abbaaad, find the longest commont subsequence between these two sequences, in these two sequences, the LCS should be abaad

  

**Intuition**:

- Consider any two sequence L and S with i and j elements, if we attempt to add a new char to i, this new character has two possibilities

  - Case 1: if it is the same as the last char in j:

    - Then the longest common subsequence will be the longest common subsequence up untill the second to the end element of S plus 1
    - i.e dp(i + 1)(j) = dp(i)(j - 1) + 1

  - Case 2: if it is not the same as the last car in the end

    - Then the longest common subsequence will be the longest common subsequence up until i or longest common subsequence till j - 1
    - i.e. dp(i + 1)(j) = max(dp(i)(j), dp(i + 1)(j - 1))

    

**Proof of Intuition**:

- For case 1, assume by contradiction that if we try to add a new char x to i that is the same as the ending char of S and our algorithm doesn't give the optimal solution
- Then, there are two cases:
  - it is matched with the ending char at S, then obviously adding one to the problem with i and j - 1 elements in L and S could produce the optimal solution, contradiction
  - it is not mached with the ending char at S, then it must be matched with some previous chars in S, so it is still 1 more than the optimal solution of the problem dp(i)(j - 1) (since at this time we don't consider the jth element), contradiction
  - We use proof by contradiction here to show that our solution is at least as best as the assumption
- When x is not equal to the ending char at S, say y
  - Then one solution to be considered is the optimal solution without y, since these cannot be matched
  - Another solution is to consider not taking x.
  - We choose to leave one depending on which gives us the better result



**Algorithm:**



### Question 7: Combination Sum IV

**Problem:** Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

**Intuition:**

- This question is essentially pretty easy: when you pick a number num, you need to check whether or not the remaining number could reach target - num
- So, the simple recursion would be if target == 0, return 1; else: return comb4(nums, target - num) for every num in nums if target >= num (if not, there is no way so it is 0 by default)
- However, using DP, we could simpify this process. Let's say we want to accumulate to target because we need to reach the target at some point. So, dp[i] is essentially solving the question: how many ways we could reach target i?
- So, the base case for dp should be 1, and any inductive step should consider every num in nums including itself.



**Code:**

```python
def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]
```




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



**Example 2: Unique Binary Search Trees**: https://leetcode.com/problems/unique-binary-search-trees/

**Example 3: Minimum Path Sum (medium):** https://leetcode.com/problems/minimum-path-sum/

Given a *m* x *n* grid filled with non-negative numbers, find a path from top left to bottom right which *minimizes* the sum of all numbers along its path.

**Note:** You can only move either down or right at any point in time.

```python
def minPathSum(self, grid: List[List[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        grid[0][i] += grid[0][i-1]
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]
```

Example





### 











