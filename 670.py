class Solution:
    """
    >>> Solution().maximumSwap(2736)
    7236
    >>> Solution().maximumSwap(9973)
    9973
    >>> Solution().maximumSwap(9478)
    9874
    >>> Solution().maximumSwap(98756)
    98765
    >>> Solution().maximumSwap(1993)
    9913
    """
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        length = len(digits)
        for pos in range(length - 1):
            swap = pos + 1
            swap_max = digits[pos + 1]
            for i in range(pos + 2, length):
                if digits[i] >= swap_max:
                    swap = i
                    swap_max = digits[i]
            if swap_max > digits[pos]:
                digits[pos], digits[swap] = digits[swap], digits[pos]
                break
        return int(''.join(digits))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
