class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        for i in range(x):
            if i*i == x:
                return i
            if i*i > x:
                return i-1
        return x - 1