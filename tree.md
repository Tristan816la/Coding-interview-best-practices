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



Now, we've walkthroughed all the traversals of a tree. Let's see if there is any application for these vital traversals.

### Tree Traversal Applications

If you can traverse an entire tree, especially a BST, there are several properties that you can use for the result of your traversal.

**Example 1: Validate Binary Search Tree:** https://leetcode.com/problems/validate-binary-search-tree/

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

```python
def isValidBST(root: TreeNode) -> bool:
    if not root:
        return True
    
    stack = []
    inorder = []
    while root or stack:
        while (root):
            stack.append(root)
            root = root.left
        
        root = stack.pop()
        inorder.append(root.val)
        root = root.right
        
    def isSorted(x):
        for i in range(len(x) - 1):
            if x[i] >= x[i + 1]:
                return False
        return True
    
    return isSorted(inorder)
```


Analysis:

If we are going to determine if a tree is a BST, we can do an inorder traversal and see if the result is in increasing order, which is the basic logic for this solution.



## Recursion On Tree

Using recursion, tree problems sometimes could be really easy to solve. I actually only think recursion is only the best practice to use if the input is a tree. (Because usually you could use other data structures like stack to mimic the effects of recursion, which would be even faster)



**Example 1: invert Binary Tree (easy):** https://leetcode.com/problems/invert-binary-tree/

```python
def invertTree(root: TreeNode) -> TreeNode:
    if not root:
        return root
    
    right = self.invertTree(root.right)
    left = self.invertTree(root.left)
    
    root.right, root.left = left, right
    
    return root
```
Analysis:

Pretty simple and the code speaks itself. Just want to show how easy it is if you use recursion on tree to solve a problem.



**Example 2:  Symmetric Tree (easy):** https://leetcode.com/problems/symmetric-tree/

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree `[1,2,2,3,4,4,3]` is symmetric:

```  python
# Recursion
def isSymmetric(self, root):
    if not root:
      return True
    else:
      return self.isMirror(root.left, root.right)

  def isMirror(self, left, right):
    if not left and not right:
      return True
    if not left or not right:
      return False
		if left.val == right.val:
      outPair = self.isMirror(left.left, right.right)
      inPiar = self.isMirror(left.right, right.left)
      return outPair and inPiar
    else:
      return False
    
# Iterative
def isSymmetric(root: TreeNode) -> bool:
  if not root:
    return True
  stack = [(root.left, root.right)]

  while stack:
    l, r = stack.pop()
    if not l and not r:
      continue
    if not l or not r:
      return False
    if l.val != r.val:
      return False

  	stack.append((l.left, r.right))
   	stack.append((l.right, r.left))

  return True
```

The idea for both iterative and recursion are the same. So, I'm going to explain the recursion.

For each left-and-right-child pair, we only need to consider if the outer pair and inner pair are the same. If any one of them is not the same, then this tree is not symmetric. Pretty simple solution



**Example 3: Lowest Common Ancestor of a Binary Tree (medium):** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”

```python
def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root: return None
    
    if p == root or q == root:
        return root
      
    left = lowestCommonAncestor(root.left, p , q)
    right = lowestCommonAncestor(root.right, p , q)
    
    if not left:
        return right
    if not right:
        return left
      
    return root
```
**Analysis:**

There are three cases for this question, what you need to do is to identify the cases:

1) Find both on the left and on the right

2) Couldn't find p, q on the left, p and q must be on the right

3) Couldn't find p, q on the right, p and q must be on the left

So, for our base cases, if we find p or q, we would return it as we are using recursion to search for p and q (Also, it is logically correct as if we find p or q as root at a given node, the other p or q is definitely a descendant of it if we let p or q be a descendant of itself).



**Example 4: Diameter of Binary Tree (easy):** https://leetcode.com/problems/diameter-of-binary-tree/

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.

```python
def diameterOfBinaryTree(root: TreeNode) -> int:
    def height(root, h):
        if not root:
            return 0
        
        left = height(root.left, h)
        right = height(root.right, h)
        
        h[0] = max(left + right, h[0])
        
        return max(left, right) + 1 # returning the height of root
    
    h = [0]
    height(root, h)
    
    return h[0]
```
**Analysis:** 

The idea behind the recursion is that we need to identify that the longest path could suffice the condition below:

Although the longest path doesn't have to go through the root node, it has to pass the root node of some subtree of the tree (because it has to be from one leaf node to another leaf node, otherwise we can extend it for free). The longest path that passes a given node using the ROOT node is T = left_height + right_height. So you just calculate T for all nodes and output the max T. (From: https://leetcode.com/problems/diameter-of-binary-tree/discuss/101132/Java-Solution-MaxDepth)



**Example 5: Balanced Binary Tree (Easy):** https://leetcode.com/problems/balanced-binary-tree/

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

> a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.

```python
def isBalanced(root: TreeNode) -> bool:
    def dfs(root):
        if not root:
            return 0
        
        l = dfs(root.left)
        r = dfs(root.right)
        
        if l < 0 or r < 0 or abs(l - r) > 1:
            return -1
        
        return max(l, r) + 1
    
    return dfs(root) != -1
  
```
**Analysis:**

A tree is balanced only if its left and right subtrees of every node differ in height by no more than 1. So, we can do a recursion on every node and see if the left and right subtrees' height difference is bigger than 1.



The if-statement and return value may be confusing, let's walkthrough them. For the if-statement, if l and r < 0 means since left or right subtrees of a node is not balanced, the tree rooted by this node is definitely not balanced, so we could return -1. Also, if the height difference between left and right is larger than 1, we should return -1 since it doesn't satisfy the balanced condition. Moreover, the return value is indeed returning the height of the tree because we are essentially comparing the height of left and right subtrees and reach a conclusion. 



The height of a tree is determined by maximum height of left and right subtrees + 1 (root itself is one unit higher than the max).



**Example 6: Binary Search Tree to Greater Sum Tree (medium):** https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

Given the `root` of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

As a reminder, a *binary search tree* is a tree that satisfies these constraints:

- The left subtree of a node contains only nodes with keys **less than** the node's key.
- The right subtree of a node contains only nodes with keys **greater than** the node's key.
- Both the left and right subtrees must also be binary search trees.

```python
def bstToGst(self, root: TreeNode) -> TreeNode:
    def helper(root, val):
        if not root:
            return val
            
        right = helper(root.right, val)
        root.val += right
        left = helper(root.left, root.val)
        return left
    
    helper(root, 0)
    
    return root
```
**Analysis:** 

## Path in Tree

Paths in tree problem are definitely those harder question. Usually, you are given a tree, but you have to find some paths that may not even use the root. This type of problem requires deep understanding of path finding methods, which includes but not limited to dfs and bfs.



Example 1: Path Sum (Easy):

Example 2: Path Sum II (Medium):



Example 3: Binary Tree Maximum Path Sum (hard): https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a **non-empty** binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.



**Example 4: Longest Univalue Path in Binary Tree (Medium):** https://leetcode.com/problems/diameter-of-binary-tree/

**Problem:** Given the `root` of a binary tree, return *the length of the longest path, where each node in the path has the same value*. This path may or may not pass through the root.

**The length of the path** between two nodes is represented by the number of edges between them.

**Analysis:**





