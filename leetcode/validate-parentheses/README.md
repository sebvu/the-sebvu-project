You are given a string `s` consisting of the following characters: `(`,`)`,`{`,`}`,`[`and`]`.

The input string `s` is valid if and only if:

1. Every open bracket is closed by the same type of close bracket.
2. Open brackets are closed in the correct order.
3. EVery close bracket has a corresponding open bracket of the same type.

Return `true` if `s` is a valid string, and `false` otherwise.

**Example 1:**

```python
Input: s = "[]"

Output: true
```

**Example 2:**

```python
Input: s = "([{}])"

Output: true
```

**Example 3:**

```python
Input: s = "[(])"

Output: false
```

Explanation: The brackets are not closed in the correct order.
