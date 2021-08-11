# Backtracking

**Example 1: Jump Game III (medium):** https://leetcode.com/problems/jump-game-iii/

Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, check if you can reach to **any** index with value 0.

Notice that you can not jump outside of the array at any time.

**Analysis:**

We'll use backtracking, with a set to keep track of visited, the ideas are simple:

- If during the backtracking we land on a pos with value 0, then we could reach to any one index with value 0

- Otherwise, we return backtrack(pos - step) and backtrack(post + step) to reflect on whether the sub steps could reach any one index with value 0

- If we happen to revisit a node, it means we cannot find a solution, return false

  

**Solution 1:**

```python
def canReach(self, arr: List[int], start: int) -> bool:
  visited = set()
  def backtrack(pos):
    if pos > len(arr) - 1 or pos < 0:
      return False
    if arr[pos] == 0:
      return True
    if pos in visited:
      return False
    visited.add(pos)
    return backtrack(pos + arr[pos]) or backtrack(pos - arr[pos])

  return backtrack(start)
```



**Example 2: Generate Parentheses (Medium):** https://leetcode.com/problems/generate-parentheses/

Given `n` pairs of parentheses, write a function to *generate all combinations of well-formed parentheses*.

**Analysis:**

This is like forming all the combinations of well-formed parentheses, and we could use backtracking to generate these parentheses fairly easily

In our backtracking function, we need to keep track of several variables

- Paren: current parenthesis combinations
- left, right: how many left and right parenthesis we have
- n: total pairs, we need to let left and right reach n in the end
- Then the idea becomes simple
  - Base case: if our len of parenthesis is 2 times of n, then we generate a valid parenthesis
  - If left < n: then we could generate more left parenthesis
  - If right < left: then we need to generate more right parenthesis to maintain the well-form



**Solution:**

```python
def generateParenthesis(self, n: int) -> List[str]:
    res = []
    self.backtrack('', res, n, 0, 0)
    return res

def backtrack(self, paren, res, n, left, right):
    if len(paren) == n << 1:
        res.append(paren)
        return
    if left < n:
        self.backtrack(paren + '(', res, n, left + 1, right)
    if right < left:
        self.backtrack(paren + ')', res, n, left, right + 1)
```