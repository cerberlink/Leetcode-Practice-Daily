"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution:
    def twoSum(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            difference = target - num
            if difference in values:
                return [i, values[difference]]
            values[num] = i
        return []


n = [2, 7, 11, 15]
k = 9
print(Solution().twoSum(n, k))
