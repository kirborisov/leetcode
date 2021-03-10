"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
"""
import pytest


class Solution:
    def reverse(self, x: int) -> int:
        output = int(str(abs(x))[::-1])
        output = -1*output if x<0 else output

        if not (-2**31 <= output <= (2**31)-1):
            return 0

        return output



def test_reverse():
    ans = Solution().reverse(123)
    assert ans == 321

    ans = Solution().reverse(-123)
    assert ans == -321

    ans = Solution().reverse(120)
    assert ans == 21

    ans = Solution().reverse(0)
    assert ans == 0

    ans = Solution().reverse(1534236469)
    assert ans == 0
