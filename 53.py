from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        >>> Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        6
        >>> Solution().maxSubArray([1])
        1
        >>> Solution().maxSubArray([5,4,-1,7,8])
        23
        """
        best_sum = -10**5
        current_sum = 0
        for x in nums:
            current_sum = max(current_sum + x, x)
            best_sum = max(best_sum, current_sum)
        return best_sum

if __name__ == "__main__":
    import doctest
    doctest.testmod()
