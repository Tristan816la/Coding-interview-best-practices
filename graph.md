## Graph



**Example 1: Clone Graph**: https://leetcode.com/problems/clone-graph/

Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph.

Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph.

Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Solution**:

```python
from collections import deque

def cloneGraph(self, node: 'Node') -> 'Node':
	if not node:
		return None
	queue = deque([node])
  visited = collections.defaultdict(Node)
  visited[node.val] = Node(node.val, [])
  while queue:
  	cur = queue.popleft()
  for nbr in cur.neighbors:
  	if nbr.val not in visited:
  		queue.append(nbr)
  		visited[nbr.val] = Node(nbr.val, [])
  	visited[cur.val].neighbors.append(visited[nbr.val])

  return visited[node.val]
```
**Analysis:**

In this solution, we create a copy of the graph using BFS. Since the values are unique for each node, we could use the nodes' values as keys. Then, we pretty much just traverse the graph and update the neighboring relationship for the copy



**Example 2: Find Redundant Connection (medium)**: 

In this problem, a tree is an **undirected** graph that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.

The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[u, v]` with `u < v`, that represents an **undirected** edge connecting nodes `u` and `v`.

Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge `[u, v]` should be in the same format, with `u < v`.



**Solution:**

```python
def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
  def dfs(s, t, visited):
    if s in visited:
      return False
    if s == t:
      return True
    visited.add(s)
    for nbr in adjList[s]:
      if dfs(nbr, t, visited):
        return True
      visited.remove(s)
    return False

    maxv = 0
    for e in edges:
      maxv = max(e[0], e[1], maxv)

    adjList = [set() for _ in range(maxv + 1)]
    res = None
    
    for edge in edges:
      	s, t = edge
        if dfs(s, t, set()):
            res = edge
            adjList[s].add(t)
            adjList[t].add(s)

   	return res
```

**Analysis:**





**Example 3: Course Schedule IV (medium)**: https://leetcode.com/problems/course-schedule-iv/

There are a total of `n` courses you have to take, labeled from `0` to `n-1`.

Some courses may have direct prerequisites, for example, to take course 0 you have first to take course 1, which is expressed as a pair: `[1,0]`

Given the total number of courses `n`, a list of direct `prerequisite` **pairs** and a list of `queries` **pairs**.

You should answer for each `queries[i]` whether the course `queries[i][0]` is a prerequisite of the course `queries[i][1]` or not.

Return *a list of boolean*, the answers to the given `queries`.

Please note that if course **a** is a prerequisite of course **b** and course **b** is a prerequisite of course **c**, then, course **a** is a prerequisite of course **c**.

```python
def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    courses = [set() for _ in range(n)]
    for p in prerequisites:
        pre, c = p
        courses[c].add(pre)

    def dfs(s, t, visited):
        if s == t:
            return True
        if s in visited:
            return False
        visited.add(s)
        for nbr in courses[s]:
            if dfs(nbr, t, visited):
                return True
        return False

    res = []
    for q in queries:
        f, s = q
        res.append(dfs(s, f, set()))
    return res
```
 **Analysis:**

- This is essentially a graph traversal using the dfs algorithm. For each of the course, we firstly up date the given prerequisite information, then we will verify whether a given course A has a course B as prereq
- For our dfs function, if s == t, it means that the start is equal to the end, and we find our requisite, else if the s is in visited, it means that we have visited this point and this route is not applicable
- For any of the neighbor of a given point s, if the neighbor is reachable to t, s is reachable to t, so we return true in this case, else we return false

