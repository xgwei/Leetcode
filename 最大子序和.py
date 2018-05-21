class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = nums[0]
        acc = nums[0]
        for i in range(1, len(nums)):
            if acc < 0:
                acc = nums[i]
            else:
                acc = acc + nums[i]
            maxs = max(maxs,acc)
        return maxs
