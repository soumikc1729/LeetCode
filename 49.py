from typing import List
from itertools import groupby

class Solution:
    """
    >>> Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    [['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
    >>> Solution().groupAnagrams([""])
    [['']]
    >>> Solution().groupAnagrams(["a"])
    [['a']]
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        original_with_sorted_str = [(''.join(sorted(s)), s) for s in strs]
        original_with_sorted_str = sorted(original_with_sorted_str, key=lambda x: x[0])
        groups = []
        for _, g in groupby(original_with_sorted_str, lambda x: x[0]):
            groups.append(list(map(lambda x: x[1], g)))
        return groups

if __name__ == "__main__":
    import doctest
    doctest.testmod()
