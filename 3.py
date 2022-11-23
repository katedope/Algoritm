class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*len(obstacleGrid[0]) for i in range(len(obstacleGrid))]
        dp[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==0:
                    dp[i][j]+=dp[i-1][j] if i-1>=0 else 0
                    dp[i][j]+=dp[i][j-1] if j-1>=0 else 0
        return dp[-1][-1]