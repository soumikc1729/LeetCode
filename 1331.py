from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        """
        >>> Solution().arrayRankTransform([40,10,20,30])
        [4, 1, 2, 3]
        >>> Solution().arrayRankTransform([100,100,100])
        [1, 1, 1]
        >>> Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12])
        [5, 3, 4, 2, 8, 6, 7, 1, 3]
        """
        if len(arr) == 0:
            return []
        sorted_indexed_arr = sorted(enumerate(arr), key=lambda x: x[1])
        ranked_arr = [1 for _ in arr]
        current_rank = 1
        prev = sorted_indexed_arr[0][1]
        for x in sorted_indexed_arr[1:]:
            if x[1] == prev:
                ranked_arr[x[0]] = current_rank
            else:
                current_rank += 1
                ranked_arr[x[0]] = current_rank
            prev = x[1]
        return ranked_arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
        