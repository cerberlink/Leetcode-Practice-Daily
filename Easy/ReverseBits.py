"""
Reverse bits of a given 32 bits unsigned integer.

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

Note:

Note that in some languages such as Java, there is no unsigned integer type. In this case, both input and output will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 2 above the input represents the signed integer -3 and the output represents the signed integer -1073741825.


Follow up:

If this function is called many times, how would you optimize it?
"""


class Solution:
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result = result << 1 ^ (n & 1)
            n >>= 1
        return result
