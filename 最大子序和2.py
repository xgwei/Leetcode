class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def msum(nums):
            if len(nums)==1:
                return [1,nums[0]]
            if len(nums)==2:
                tmp = msum(nums[0:-1])
                if tmp[0]==1:
                    return max
        
        
        
        cur=[nums[0]]
        cur_val = nums[0]
        direction = 0
        cont = 0
        rec_val = cur_val-1
        for i in range(1,len(nums)):
            if nums[i]>=0:
                if cur_val<0:
                    cur=[nums[i]]
                    cur_val=nums[i]
                    cont = 1
                elif cur_val>=0:
                    cur=cur+[nums[i]]
                    cur_val=cur_val+nums[i]
                    cont = 1
            elif nums[i]<0:
                if cur_val>=rec_val:
                    rec=cur
                    rec_val=cur_val
                if cont == 1:
                    if cur_val+nums[i]>0:
                        cur=cur+[nums[i]]
                        cur_val=cur_val+nums[i]
                        cont = 1
                    else:
                        cur = []
                        cur_val = 0
                        cont = 0
            print(rec)
        return rec_max
