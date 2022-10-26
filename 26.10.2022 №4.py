class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def a(c, d, f):

            if c > 0:
                return a(c // d, d, f + (
                            c % d))  # пока с больше 0, мы делим с на д, а в f пихаем остаток от деления с на d и сразу плюсуем это
            else:
                return f

        return a(n, k, 0)
# сложность O(log(n))