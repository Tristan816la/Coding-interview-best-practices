# Array



**Example 1: String sum (medium) (Adapted from mock coding interview question)**

- Given an array of string arr, given two index i and j (i could be equal to j), return the sum of string representation of arr[i] + arr[j]
- For instance, assume arr = [2, 10], arr[0] ''+'' arr[0] = 22, arr[0] "+" arr[1] = 210, arr[1] "+" arr[0] = 102, arr[1] "+" arr[1] = 1010, so the result should be 1010 + 102 + 210 + 22 = 1344

Time exceeded Brute-force solution (O(n^2)):

```python
def stringsum2(arr):
    res = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            res += int(str(arr[i]) + str(arr[j]))
    return res
```

Real solution (O(nk), k is the length of the number with max digits):

```python
def stringsum(arr):
    maxWidth = 0
    res = 0

    for i in arr:
        if len(str(i)) > maxWidth:
            maxWidth = len(str(i))

    buckets = [0 for i in range(maxWidth + 1)]

    for i in arr:
        buckets[len(str(i))] += 1

    for el in arr:
        res += el * len(arr)
        for i in range(1, len(buckets)):
            res += el * buckets[i] * 10 ** i
    return res
```

Analysis:

This solution applies the idea of couting sort (bucket sort) we learned in sorting chapter. First, we find the number with the most digit. Then, we create buckets with size of maxWidth + 1, storing every 