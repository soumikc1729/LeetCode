from typing import List

class Solution:
    """
    >>> Solution().generateParenthesis(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    >>> Solution().generateParenthesis(1)
    ['()']
    """
    def generateParenthesis(self, n: int) -> List[str]:
        parenths = []
        self.generate(n, n, [], parenths)
        return parenths
    
    def generate(self, left: int, right: int, cur: List[str], parenths: List[str]):
        if right < left:
            return
        if left == 0 and right == 0:
            parenths.append(''.join(cur))
            return
        if left > 0:
            cur.append('(')
            left -= 1
            self.generate(left, right, cur, parenths)
            left += 1
            cur.pop()
        if right > 0:
            cur.append(')')
            right -= 1
            self.generate(left, right, cur, parenths)
            right += 1
            cur.pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod()
