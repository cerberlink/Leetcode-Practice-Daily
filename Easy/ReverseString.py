"""
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]


["h","e","l","l","o"]
  l               r

["o","e","l","l","h"]
      l       r

["o","l","l","e","h"]
          lr
execution termination!


l = left
r = right


two-pointers approach is easy one. 

algorithm:
1. use the while loop to iterate left and right
2. use the swap 
3. keep moving left and moving right.
"""

# Algorithm Analysis: O(n) time | O(1) space

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # use two pointers
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]  # swap
            left += 1  # move to another one in left
            right -= 1  # move to another one in right


input = ["h", "e", "l", "l", "o"]

print(Solution().reverseString(input))
