from typing import List
from functools import reduce

class Solution:
    """
    >>> Solution().singleNumber([2,2,1])
    1
    >>> Solution().singleNumber([4,1,2,1,2])
    4
    >>> Solution().singleNumber([1])
    1
    """
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums, 0)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
