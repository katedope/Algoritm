class Solution:
    def numberOfMatches(self, n: int) -> int:
        def a(c, d):
            if c == 1:
                return d
            return a(c / 2, d + (c / 2)) if c % 2 == 0 else a((c - 1) / 2 + 1, d + ((c - 1) / 2))

        return int(a(n, 0))

# сложность O(log(n))