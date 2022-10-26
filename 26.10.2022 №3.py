class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        def a(c, d):
            s = 0
            for i in d:
                if i in c:
                    s = s + 1
            return s

        return a(jewels, stones)

# сложность O(n)