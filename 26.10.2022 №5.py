class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        li = []
        ind = []
        ls = list(s)
        for i in range(0, len(s)):  # идем перебирать i по s
            if len(li) == 0:  # если стек = 0, то в ind пихаем i, а в стек пихаем s[i]
                ind.append(i)
                li.append(s[i])
            elif s[i] == '(':  # если s[i] = (, то мы пихаем s[i] в стек
                li.append(s[i])
            elif s[i] == ')' and len(
                    li) > 1:  # а если s[i] = ) и стек не пустой, тто мы удаляем последний элемент стека
                li.pop()
            elif len(li) == 1 and s[
                i] == ')':  # если длинна стек = 1 и s[i] = ), то в индекс пихаем i, а стек обнуляем
                ind.append(i)
                li.pop()

        rind = ind[::-1]  # берем срез с конца, чтобы индексы не менялись
        a = ''
        for i in range(len(rind)):  # проходим по этому срезу и удаляем лишнее
            ls.pop(rind[i])
        for i in ls:  # чтобы вывсти строку, кидаем все что есть в списке в переменную а
            a += i
        return a
# сложность O(len(s))
