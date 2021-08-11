# Stack and Queue Ultimate

Stack and Queue are commonly used data structure. Below is a list of scenarios that you'll use either a stack or a queue



### Stack

1. Parenthese Matching
2. Reversed linked list manipulation (Not reverse a linked list)
3. String manipulation (Character Matching)
4. DFS
5. Tree: inorder traversal

### Queue

1. BFS
2. Tree: level order traversal





#### Stack Examples:

Example 1: 

**Example 2: Daily Temperature (Medium):** https://leetcode.com/problems/daily-temperatures/



**Example 3: Basic Calculator II:** https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero.

Solution from: https://leetcode.com/problems/basic-calculator-ii/discuss/443590/python-stack

```python
def calculate(self, s: str) -> int:
  num = 0
  res = 0
  pre_op = '+'
  s+='+'
  stack = []
  for c in s:
    if c.isdigit():
      num = num * 10 + int(c)
    elif c == ' ':
        continue
    else:
        if pre_op == '+':
          stack.append(num)
        elif pre_op == '-':
          stack.append(-num)
        elif pre_op == '*':
          operant = stack.pop()
          stack.append((operant*num))
        elif pre_op == '/':
          operant = stack.pop()
          stack.append(math.trunc(operant/num))
          num = 0
          pre_op = c
  return sum(stack)
```

This is indeed a really smart solution (wooh to the author). This



Example 4: Asteroid Collision https://leetcode.com/problems/asteroid-collision/