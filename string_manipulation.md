# String Manipulation

String is a relatively interesting topic in coding interview. Due to the immutability of string, we can not treat it as a linked list where we can change any char as we are changing a node. It is more like an array, and topics invovle with string are frequently shown up in real coding interview.



Let's dive into the examples to see how strings are tested in coding interviews.



**Example 1: Chemical Equation Balanced or not (medium hard) (Adapted from real interview):**

- Given a string representing a chemical equation, identify whether two sides of equation is balanced or not.

e.g. "2H2 + O2 = 2H2O": True, because both sides have four H and 2 O.

Things to notice:

- We use capital letter to represent an element, and lower-case letter should be a part of the name. For instance, H is an element, Re is an element, Hooooooooo is an element.
- The number behind the element represents the number of this element, but we also need to take into account of the constant in the front. For instance, in 2H2O, there are 2 * 2 = 4 H, and 2 O.

- Assume the given string is always valid

```python
import collections


def balance(s):
    s.replace(" ", "")
    left, right = s.split("=")
    leftEl = left.replace(" ", "").split("+")
    rightEl = right.replace(" ", "").split("+")
    leftCounter = collections.Counter()
    rightCounter = collections.Counter()
    for el in leftEl:
        balanceEl(el, leftCounter)
    for el in rightEl:
        balanceEl(el, rightCounter)
    return not (rightCounter - leftCounter)


def balanceEl(el, counter):
    const = ''
    elName = ''
    count = ''
    flag = True
    for j in range(len(el)):
        if flag and el[j].isdigit():
            const += el[j]
            continue
        else:
            flag = False
        if el[j].islower():
            elName += el[j]
        if j > 0 and el[j].isdigit():
            count += el[j]
        if el[j].isupper():
            if elName != '':
                if count == '':
                    count = '1'
                counter[elName] += int(count) * int(const)
                count = ''
            elName = el[j]
        if j == len(el) - 1:
            if elName != '':
                if count == '':
                    count = '1'
                counter[elName] += int(count) * int(const)
                count = ''
            elName = el[j]

```



Analysis:

This question doesn't require any smart trick. The idea for solving this problem is pretty simple: we count the elements at the left side and right side, and see if they have the same counts. But this problem indeed require a really good familiarity with string and solution planning.



First, we delete all the spaces between characters. Second, we split each portion by "+". Third, we count each element's count in each portion by using python's counter. Fourth, we check if the left counter and right counter are the same to reach the conclusion on whether they have the same count.



The tricky part is the third step. We use the idea of stack for manipulating string - storing the elments in a temp string and update every element when there is a trigger. We check the condition given by the problem and divide the cases into upper-case, lower-case, digit, and front constants.



If a problem alike shows up in a real coding interview, remember to divide the problem into small cases and tackle them from ground up. Also, familiarize youself with the string function in python, which can be found in this site:

https://docs.python.org/2/library/string.html#string-functions



So by reading the solution of this problem, you should notice:

1. Strings, just like a stack, are really easy to check and manipulate if you set clear condition
2. Using data structure like hash map or counter would be really helpful for solving the string problem.



**Example 2: Add Binary (Easy):** https://leetcode.com/problems/add-binary/

- Given two binary strings, return their sum (also a binary string).

- The input strings are both **non-empty** and contains only characters `1` or `0`.

```python
def addBinary(self, a: str, b: str) -> str:
  carry = 0
  result = ''

  a = list(a)
  b = list(b)

  while a or b or carry:
    if a:
      carry += int(a.pop())
    if b:
      carry += int(b.pop())
    result += str(carry % 2)
    carry //= 2

 	return result[::-1]
```

Analysis:

First, notice python list() function could change a string to a character list which contains every char in the string. Then, we are essentially using a and b as a stack. So since character is either '0' or '1', our carry could only be '0', '1', and '2'. So, for instance, if a = 1101 and b = 1100. We are goding to have carry = 1, at first, result = 1 % 2 = 1.  Carry then reset to 0. For carry = 0, it is the same. If carry = 2, it means we need to carry one to the next digit. For instance in at a[1] and b[1], since they sum to two, we carry 1 to a[0] and b[0]. In the end, if there is carry left, it means that we need to add one more digit. In this example, the result should be 11001, which has one more digit to carry.



**Example 3: Reverse words in a string (medium): **https://leetcode.com/problems/reverse-words-in-a-string/

- Given an input string, reverse the string word by word.
- Your reversed string should not contain leading or trailing spaces.
- You need to reduce multiple spaces between two words to a single space in the reversed string.

```python
def reverseWords(self, s: str) -> str:
  	words = []
    st = ""
        
    for i, char in enumerate(s):
      if char == " " and st != "":
        words.append(st)
        st = ""
      elif char != " ":
        st += char
                
    if st != "":
      words.append(st)
            
    words.reverse()
    return ' '.join(words)
```

Analysis: 

For this example, we use a similar approach that we've used in the balancer question. We keep track of a st variable, and when we hit a space, we'll check if st is "". If not, which means we have stored a string, then we gonna add it to the words list. And if the char is not a space, we gonna add it to st. Then after having the words list, we can reverse it and join every element with a space.



**Example 4: Add Strings (Easy)**: https://leetcode.com/problems/add-strings/

 Given two non-negative integers `num1` and `num2` represented as string, return the sum of `num1` and `num2`.

1. The length of both `num1` and `num2` is < 5100.
2. Both `num1` and `num2` contains only digits `0-9`.
3. Both `num1` and `num2` does not contain any leading zero.
4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

```python
def addStrings(self, num1: str, num2: str) -> str:
  carry = 0
  result = ""
  num1, num2 = list(num1), list(num2)
  zero = ord('0')

  while num1 or num2 or carry:
    if num1:
      carry += (ord(num1.pop()) - zero)
    if num2:
      carry += (ord(num2.pop()) - zero)
    if carry >= 10:
      result += chr(zero + carry - 10)
      carry = 1
    else:
      result += chr(zero + carry)
      carry = 0

  return result[::-1]
```

Analysis:

Since this example is really similar to example 2, I wouldn't spend too much time explaining this solution. The reason why I pick this problem is the usage of chr() and ord() in python. ord() returns the order to the character in the Ascii, and chr() returns the character by giving the order.



## Trie

The section before wrapping up common patterns of the string problem. However, there is one data structure relavant to string that is great to learn -- Trie. Trie, also known as prefix tree, is a data structure commonly used to utilize the properties of prefix for a list of strings. Let's see its implementation and one application of this data structure.



**Example 1:  Implement Trie (Prefix Tree):** https://leetcode.com/problems/implement-trie-prefix-tree/

- Implement a trie with `insert`, `search`, and `startsWith` methods.

```python
class TrieNode:
    def __init__(self):
        self.isWord = False
        self.children = collections.defaultdict(TrieNode)
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr_node = self.root
        for c in word:
            curr_node = curr_node.children[c]
        curr_node.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return curr_node.isWord       

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr_node = self.root
        for c in prefix:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return True

```

Analysis:

Above is the implementation of trie. Notice that since we are using collections.defaultdict(TrieNode) for children, if there is no trienode in the dict, it would automatically create one Node for us and map the Node with coressponding key.









