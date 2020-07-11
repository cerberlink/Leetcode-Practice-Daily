"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.


"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # result
        result = 0
        # a while loop for n
        while x > 0 or y > 0:
            # compute the actual numbers into binary and evaluate them in XOR (^)
            result += (x % 2) ^ (y % 2)
            # right shift for bits
            x >>= 1
            y >>= 1
        return result


x, y = 1, 4
print(Solution().hammingDistance(x, y))
