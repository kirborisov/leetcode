"""
Given two strings a and b, return true if you can swap two letters in a so \
the result is equal to b, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that \
i != j and swapping the characters at a[i] and b[j]. For example, swapping at indices\
0 and 2 in "abcd" results in "cbad".
"""
import pytest


class Solution:
    def buddyStrings(self, a: str, b: str) -> bool:
        # Constraints
        if not (1 <= len(a), len(b) <= 2*104 ):
            return False
        if not (a.islower() and b.islower()):
            return False
        if len(a) != len(b):
            return False

        d_l = list(filter(lambda x: x, map(lambda x,y: None if x==y else [x,y], a, b)))
        if not d_l and len(set(a)) != len(a):
            return True
        elif len(d_l) != 2:
            return False
        elif d_l[0] != d_l[1][::-1]:
            return False
        else:
            return True

def test_solution():
    ans = Solution().buddyStrings('ab', 'ba')
    assert ans == True

    ans = Solution().buddyStrings('ab', 'ab')
    assert ans == False

    ans = Solution().buddyStrings('aa', 'aa')
    assert ans == True

    ans = Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb')
    assert ans == True
