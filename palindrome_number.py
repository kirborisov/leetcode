"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.\
For example, 121 is palindrome while 123 is not.
"""
import pytest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if not (-2**31 <= x <= (2**31)-1 ):
            return False
        return True if str(x) == str(x)[::-1] else False



def test_solution():
    ans = Solution().isPalindrome(121)
    assert ans == True

    ans = Solution().isPalindrome(-121)
    assert ans == False

    ans = Solution().isPalindrome(10)
    assert ans == False

    ans = Solution().isPalindrome(-101)
    assert ans == False

    ans = Solution().isPalindrome(2**32)
    assert ans == False
