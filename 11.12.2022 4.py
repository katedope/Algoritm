# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if root == None:
            return 0
        stack = [(root, 0)]
        spisok1 = [root.val]

        while stack:
            cur_vartex, vetka = stack.pop()
            spisok = []

            if cur_vartex.left != None:
                stack.append((cur_vartex.left, vetka + 1))
                spisok.append(cur_vartex.left.val)

            if cur_vartex.right != None:
                stack.append((cur_vartex.right, vetka + 1))
                spisok.append(cur_vartex.right.val)
            if len(spisok) != 0:
                spisok1.append((sum(spisok) / len(spisok)))

        return spisok1