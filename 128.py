from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        >>> Solution().longestConsecutive([100,4,200,1,3,2])
        4
        >>> Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1])
        9
        """
        if len(nums) == 0:
            return 0
        uf = UnionFind(len(nums))
        indices = {}
        for i, n in enumerate(nums):
            if n in indices:
                continue
            indices[n] = i
            if n - 1 in indices:
                uf.union(i, indices[n - 1])
            if n + 1 in indices:
                uf.union(i, indices[n + 1])
        return uf.max_component_size()

class UnionFind:
    def __init__(self, size: int):
        self.id = [x for x in range(size)]
        self.sz = [1 for _ in range(size)]
    
    def find(self, p: int) -> int:
        root = p
        while root != self.id[root]:
            root = self.id[root]
        
        # path compression
        while p != root:
            next = self.id[p]
            self.id[p] = root
            p = next
        
        return root
    
    def union(self, p: int, q: int):
        root1 = self.find(p)
        root2 = self.find(q)
        if root1 == root2:
            return
        
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
            self.sz[root1] = 0
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
            self.sz[root2] = 0

    def max_component_size(self):
        return max(self.sz)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
