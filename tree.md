# Tree

Tree is a frequently tested topic in coding interview. The topic related to tree invovles binary search tree (BST), n-tree, tree path and etc. DFS and BFS are commonly used for tree problems, and recursion is also always great to use if the interviews allow.  



## Tree Traversals

There are four types of traversal - inorder, postorder, and preorder, and level order. I wouldn't explain the concepts of these traversals since they are taught everywhere. Let's dive into their implementation.



Notice: I'll not use recursion to implement these traversals since it is trivial to traverse a tree using recursion. It is also a bit harder and more interesting to come up with the way you can traverse a tree using stack and queue.



**Example 1: Binary Tree Inorder Traversal (medium):** https://leetcode.com/problems/binary-tree-inorder-traversal/

- Given the `root` of a binary tree, return *the inorder traversal of its nodes' values*.

```python
def inorderTraversal(root: TreeNode) -> List[int]:
    stack = []
    cur = root
    result = []
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left

        else:
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

    return result
```


**Example 2: Binary Tree Preorder Traversal (medium):** https://leetcode.com/problems/binary-tree-preorder-traversal/

```python
def preorderTraversal(root: TreeNode) -> List[int]:
    if not root:
        return []
    res = []
    stack = [root]
    
    while stack:
        cur = stack.pop()
        res.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return res
```
**Example 3: Binary Tree Postorder Traversal (medium):** https://leetcode.com/problems/binary-tree-postorder-traversal

```python
def postorderTraversal(self, root: TreeNode) -> List[int]:
  if not root:
    return []
  res = []
  stack = [root]

  while stack:
    cur = stack.pop()
    res.append(cur.val)
    # A "reversed preorder"
    if cur.left:
      stack.append(cur.left)
    if cur.right:
      stack.append(cur.right)
      
  return res[::-1]

# Or better:
def postorderTraversal(self, root):
    if not root:
      return []
    res, stack = [], [(root, False)]
    while stack:
      cur, visited = stack.pop()
      if visited:
        res.append(cur.val)
      else:
        # Post-order
        stack.append((cur, True))
     	  if cur.right:
          stack.append((cur.right, False))
        if cur.left:
          stack.append((cur.left, False))
   	return res
```

**Example 4: Binary Tree Level Order Traversal (medium):**  https://leetcode.com/problems/binary-tree-level-order-traversal/

```python
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
Notice we store a size because the queue's size is changing in the for-loop. Notice deque in python cannot store a tuple like list. 

Level order traversal is indeed a BFS.



