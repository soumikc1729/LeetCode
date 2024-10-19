class Solution:
    """
    >>> Solution().uniquePaths(3, 7)
    28
    >>> Solution().uniquePaths(3, 2)
    3
    """
    def uniquePaths(self, m: int, n: int) -> int:
        larger = max(m, n)
        smaller = m + n - larger
        nume = 1
        for x in range(larger, m + n - 1):
            nume *= x
        deno = 1
        for x in range(1, smaller):
            deno *= x
        return int(nume / deno)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
