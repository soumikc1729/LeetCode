from typing import List

class Solution:
    """
    >>> Solution().canArrange([1,2,3,4,5,10,6,7,8,9], 5)
    True
    >>> Solution().canArrange([1,2,3,4,5,6], 7)
    True
    >>> Solution().canArrange([1,2,3,4,5,6], 10)
    False
    """
    def canArrange(self, arr: List[int], k: int) -> bool:
        modK = [x % k for x in arr]
        modCount = {}
        for x in modK:
            if x not in modCount:
                modCount[x] = 0
            modCount[x] += 1

        # mod 0 count needs to be even
        if 0 in modCount and modCount[0] % 2 == 1:
            return False
        
        for mod in range(1, k):
            if mod in modCount:
                comp = k - mod
                if comp not in modCount or modCount[mod] != modCount[comp]:
                    return False
        return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
