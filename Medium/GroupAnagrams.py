"""
The problem is linked: https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

I found the group anagram that is the output.
eat - tea - ate

tan - nat

bat

(thoughts)
I think we need to use the hashmap that is efficiently time. that one easily finds the occurrence of anagram group. 
we need to sort the string alphabetically (a - z) in order to matched each other.
we can count them as many as we can group.

Algorithm -

1. create the hashmap as dict in python.
2. use a for loop in the array.
3. sort the string alphabetically.
4. match the anagram from group and count it as occurrence
5. return output as occurrence
"""

# Analysis time = O(n) time | O(1) space

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}  # dict
        for s in strs:
            key = tuple(sorted(s))
            hashmap[key] = hashmap.get(key, []) + [s]
        return hashmap.values()


input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(input))
