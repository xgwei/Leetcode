class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        a=nums
        dp=[ 0 for i in range(len(nums))]
        
        for i in range(len(nums)):
            Max = 0;
            for j in range(i):
                if (a[i] > a[j]):
                    #如果当前值比之前某个值大的话，至少也得是比之前这个值的序列长1了
                    Max = max(Max, dp[j])
            dp[i] = Max + 1;
        Max = 0;
        for i in range(len(nums)):
            if (dp[i] > Max):
                Max = dp[i]
        return Max
