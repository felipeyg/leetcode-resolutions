# Defina a classe Solution
class Solution:
    def numberOfMatches(self, n: int) -> int:
        p = 0
        while n > 1:
            if n % 2 == 0:
                p += n / 2
                n = n / 2
            else:
                p += 1 + (n - 1) / 2
                n = (n - 1) / 2
        return print(int(p))

Solution().numberOfMatches(14)


