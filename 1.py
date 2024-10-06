class Solution:
    """
    >>> Solution().twoSum([2, 7, 11, 15], 9)
    [0, 1]
    >>> Solution().twoSum([3, 2, 4], 6)
    [1, 2]
    >>> Solution().twoSum([3, 3], 6)
    [0, 1]
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsi = list(enumerate(nums))
        numsi.sort(key=lambda x: x[1])
        start, end = 0, len(numsi) - 1
        while start < end:
            sum = numsi[start][1] + numsi[end][1]
            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                return [numsi[start][0], numsi[end][0]]
        raise Exception("no answer found")