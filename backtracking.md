# Backtracking

Example 1: Jump Game III (medium): https://leetcode.com/problems/jump-game-iii/

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





Example 2: Generate Parentheses (Medium)