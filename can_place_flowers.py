import pytest
from typing import List
import re


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Constraints 1
        if not (1 <= len(flowerbed) <= 2 * 10**4) or not (0 <= n <= len(flowerbed)):
            return False
        
        flowerbed_str = '0{}0'.format(''.join(map(lambda x: str(x), flowerbed)))
        
        # Constraints 2
        if re.search('[^01]+', flowerbed_str):
            return False
        
        count_posible = 0
        while True:
            free_places = len(re.findall('000', flowerbed_str))
            if not free_places:
                break
            count_posible += free_places
            flowerbed_str = flowerbed_str.replace('000', '0')

        return True if count_posible >= n else False


        

def test_solution():
    ans = Solution().canPlaceFlowers([1,0,0,0,1], 1)
    assert ans == True

    ans = Solution().canPlaceFlowers([1,0,0,0,1], 2)
    assert ans == False

    ans = Solution().canPlaceFlowers([0,0,1,0,1], 1)
    assert ans == True

    ans = Solution().canPlaceFlowers([1], 1)
    assert ans == False

    ans = Solution().canPlaceFlowers([0], 1)
    assert ans == True

    ans = Solution().canPlaceFlowers([0,0,1,0,0], 1)
    assert ans == True
