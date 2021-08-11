**Example 1: Binary Tree Level Order Traversal (medium):** https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the `root` of a binary tree, return *the level order traversal of its nodes' values*. (i.e., from left to right, level by level).

```python
from collections import deque

def levelOrder(self, root):
    if not root: return []
    queue, res = deque([root]), []
        
    while queue:
        cur_level, size = [], len(queue)
        for i in range(size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            cur_level.append(node.val)
        res.append(cur_level)
    return res
```


**Example 2: Find Largest Value in Each Tree Row (medium):** https://leetcode.com/problems/find-largest-value-in-each-tree-row/

Given the `root` of a binary tree, return *an array of the largest value in each row* of the tree **(0-indexed)**.

```python
from collections import deque
def largestValues(self, root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    def bfs_largest(root):
        q = deque([(root, 0)])
        level = 0
        while q:
            cur, lev = q.popleft()
            level = max(lev, level)
            if len(res) > level:
                res[level] = max(res[level], cur.val)
            else:
                res.append(cur.val)
            if cur.left:
                q.append((cur.left, level + 1))
            if cur.right:
                q.append((cur.right, level + 1))
    
    bfs_largest(root)
    return res
```
**Analysis:**

- For this problem, we are essentially doing a level-order traversal of the tree
- But, in order to identify the level, we keep a level variable
- We directly modify the res array to save the space
- When the level is smaller than the current length of res, e.g. level 2 with length 3 res, it means that we can compare the current value in res[2] with the just visited node's value. By visiting every node and compare each node in the row to get the max, we gurantee that res[i] is having the largest value for row i
- Else, if we len(res) is smaller than level, it means we are visiting the level for the first time so we need to push one element first to the corresponding level