# String Manipulation

String is a relatively interesting topic in coding interview. Due to the immutability of string, we can not treat it as a linked list where we can change any char as we are changing a node. It is more like an array, and topics invovle with string are frequently shown up in real coding interview.



Let's dive into the examples to see how strings are tested in coding interviews.



**Example 1: Chemical Equation Balanced or not (medium) (Adapted from real interview):**

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



Example 2: Add Binary (Easy): https://leetcode.com/problems/add-binary/

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

First, notice python list() function could change a string to a character list which contains every element in the string. 



Example 3: Reverse words in a string (medium): https://leetcode.com/problems/reverse-words-in-a-string/

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

Also, for words

## Trie





