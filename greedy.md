# Greedy

A **greedy algorithm** is any algorithm that follows the problem-solving heuristic of making the locally optimal choice at each stage. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time.

(From: https://en.wikipedia.org/wiki/Greedy_algorithm)

### Characteristics

1. Simple
2. Quick
3. Easy to program

### But it sucks because:

- Locally optimal solution, not the most optimal solution



Greedy algorithms make the best choice at each decision without looking ahead. For example, think of finding the shortest path from A to B in a graph. A greedy approach is always traversing to the closest node to the current node until we hit B, but this path might not be the shortest path to B. This is the heuristic of the greedy algorithm.



But in the following chapter, we gonna discuss the situation when a greedy algorithm acutally works. Let's dive into the "greedy world" by discussing a problem that might happen in the real life.



1. **Time-slot Interval Optimization:  (medium)**

Given an interval representing your available time, and given a list of time frames that the clients request (which are all in your time interval), find the way you can have an one-on-one meeting with the most clients.



Answer:

Method 1:

Pick the intervals that finish the earliest



Method 2:

Pick the intervals that start the latest



I'll give an informal proof for method 2:

When we pick the time interval that start the latest, we gurantee that no other client have a starting time before it.

For example, if our time is 0 - 10, and the latest starting time is 8, we gurantee that no client starts later than 8. So when we try to meet the most clients in time interval 0 - 8, we are guranteed to find at least the clients in a shorter interval (let's say 0 - 7, since 0-7 is included in the interval). Thus, using induction we can prove method 2 holds.



For a more formal proof, please check this video: https://www.youtube.com/watch?v=hVhOeaONg1Y&ab_channel=BackToBackSWE

![Screen Shot 2020-09-25 at 12.22.12 AM](/Users/tristanque/Library/Application Support/typora-user-images/Screen Shot 2020-09-25 at 12.22.12 AM.png)



**Time complexity analysis**:

The Brute force approach would take O(2^n), since there are 2 options for each interval: choose or not choose



However, 

FinishEarliest algorithm will have runtime of O(nlogn): we only need to sort the end time to pick the optimal interval each time.



By doing this classic greedy problem, you can find that the greedy problem is usually only using a simple invariant, but how to find and prove this invariant might be the most difficult part. Let's do some examples on leetcode and try our best to get the intuition of the greedy algorithm.



**Example 1: Jump Game (medium)**: https://leetcode.com/problems/jump-game/

- Given an array of non-negative integers, you are initially positioned at the first index of the array. 
- Each element in the array represents your maximum jump length at that position. 
- Determine if you are able to reach the last index.

```python
def canJump(nums: List[int]) -> bool:
  last = len(nums) - 1
  for i in range(len(nums) - 2, -1, -1):
    if (nums[i] + i) >= last:
      last = i
  return last <= 0

# Or just:
def canJump_2(nums: List[int]) -> bool:
  max_j = nums[0]
  i = 0
  while i <= max_j and i < len(nums):
    max_j = max(max_j, i + nums[i])
    i += 1
    return max_j >= len(nums) - 1
```

**Analysis:** 

The first solution is to think of the problem in a reversed way. Let last be a varaible storing the last element we can reach from backward. And then we traversed nums in a reversed manner. If any element in the array can reach last or surpass last, we update the index of that element to be the last because it can reach to len(nums) - 1 we set at first. When doing the entire traversal, we only need to know if last == 0. (We mark last <= 0 to avoid len(nums) == 0)



The second solution is to think intuitively, and it is acutally a little faster. Basically, for every reachable elements in num, we try to get the maximum reachable distance from these elements. And in the end, we only need to see if the maximum reachable distance is larger than len(nums) - 1. This is faster because at any point we cannot reach the end (i.e. i > max_j but i < len(nums)), the loop will end itself, so in some cases we don't need to traverse all the elements.



**Example 2 (Challenge): Jump Game II (Hard):** https://leetcode.com/problems/jump-game-ii/

- Given an array of non-negative integers, you are initially positioned at the first index of the array.

- Each element in the array represents your maximum jump length at that position.

- Your goal is to reach the last index in the minimum number of jumps.

```python
def jump(self, nums: List[int]) -> int:
  if len(nums) <= 1: return 0
  l, r = 0, nums[0]
  times = 1
  while r < len(nums) - 1:
    times += 1
    nxt = max(i + nums[i] for i in range(l, r + 1))
    l, r = r + 1, nxt
  return times
```

Analysis:

Let's walkthrough this example see why it works. First, we keep a pointer at the starting index, and another pointer pointing to the max item that l could go to. Then, for each element between l and r, we need to find the max position we could go to. In the end, we set l to be the element after r and set r to the next most index. We increase times by one in the middle of the process.



This approach could work because given an index i, if the max element l could reach is at j, then all other elements between l and nums[i] can at most reach is j, so we find the optimal solution to go to j. We continue this process until we hit len(nums) - 1, and the times variable store the max steps we need to do to go to the end of nums.



**Example 3: Task Scheduler (medium):** https://leetcode.com/problems/task-scheduler/

Given a characters array `tasks`, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer `n` that represents the cooldown period between two **same tasks** (the same letter in the array), that is that there must be at least `n` units of time between any two same tasks.

Return *the least number of units of times that the CPU will take to finish all the given tasks*.



Greedy is hard to grasp since it needs the interviewee to come up with a solution with great intuition. However, the underlying rule of each greedy algorithm is that there is one invariant, and such invariant could incrementally build up the real solution. It definitely took some time to practice.

### (Bonus) Dijkstra's Algorithm













