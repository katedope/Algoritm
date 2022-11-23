def multikonj(listofstrings):
    res = '1'*len(listofstrings[0])
    for i in listofstrings:
        res='{0:b}'.format(int(res,2) & int(i,2))
    return '0'*(len(listofstrings[0])-len(res))+res
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        s = []
        for i in range(0, len(matrix)):
            a = ''
            for j in range(0, len(matrix[0])):
                a += str(matrix[i][j])
            s.append(a)
        data = s
        count = 0
        for i in range(1,min(len(data),len(data[0]))+1):
            for j in range(len(data)-i+1):
                konjunk = multikonj(data[j:j+i])
                for k in range(len(konjunk)-i+1):
                    if '0' not in konjunk[k:k+i]:
                        count+=1
        return count
    