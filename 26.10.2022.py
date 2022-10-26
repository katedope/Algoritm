class Solution:
    def numberOfSteps(self, num: int) -> int:
        def a(c, d):
            if c == 0:
                return d

            return a(c / 2, d + 1) if c % 2 == 0 else a(c - 1,
                                                        d + 1)  # возращаю с до того пока она не станет = 0, d - считаю количество этих возвращений

        return a(num, 0)
# сложность = О(log(n))