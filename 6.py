class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<=2:
            return max(nums)

        def max_rob(nums):
            if len(nums)<=2:
                return max(nums)
            dp=[0]*len(nums)
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(1,len(nums)):
                dp[i]=max(nums[i]+dp[i-2],dp[i-1])
            return max(dp)

        return max(max_rob(nums[:-1]),max_rob(nums[1:]))

print(Solution.rob("",[1,2,3,1]))