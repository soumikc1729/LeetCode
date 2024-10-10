from collections import deque

class Solution:
    """
    >>> Solution().isValid("()")
    True
    >>> Solution().isValid("()[]{}")
    True
    >>> Solution().isValid("(]")
    False
    >>> Solution().isValid("([])")
    True
    """
    def isValid(self, s: str) -> bool:
        opening_brackets = "([{"
        corresponding_brackets = { ")": "(", "]": "[", "}": "{"}
        stack = deque()
        for c in s:
            if c in opening_brackets:
                stack.append(c)
            elif len(stack) > 0 and corresponding_brackets[c] == stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
