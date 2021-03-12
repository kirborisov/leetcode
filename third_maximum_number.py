"""
Given integer array nums, return the third maximum number in this array. 
If the third maximum does not exist, return the maximum number.
"""

import pytest
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Constraints
        if not (1 <= len(nums) <= 10**4):
            return False
        
        s_nums = sorted(set(nums), reverse=True)[:3]
        len_s_nums = len(s_nums)
        
        # Constraints
        if not (s_nums[len_s_nums-1] >= -2**31 and s_nums[0] <= (2**31) - 1):
            return None 
        
        if len_s_nums < 3:
            return max(s_nums)
        else:
            return s_nums[2]

def test_solution():
    ans = Solution().thirdMax([3,2,1])
    assert ans == 1

    ans = Solution().thirdMax([1,2])
    assert ans == 2

    ans = Solution().thirdMax([2,2,3,1])
    assert ans == 1
