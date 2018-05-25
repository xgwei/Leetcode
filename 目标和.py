class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        
        self.lib={}
        for i in range(len(nums)):
            self.lib[i]={}
        def myfunc(self,nums,S,idx):
            if S in self.lib[idx]:
                return self.lib[idx][S]
            
            if idx==(len(nums)-1):
 #               print(S,nums[idx])

                if (S==0)&(nums[idx]==0):
                    self.lib[idx][S]=2
                    return 2
                if S==nums[idx]:
                    self.lib[idx][S]=1
                    return 1
                if S==-nums[idx]:
                    self.lib[idx][S]=1
                    return 1
                if S!=nums[idx]:
                    self.lib[idx][S]=0
                    return 0
            counter=0
            self.lib[idx][S]=counter+myfunc(self,nums,S-nums[idx],idx+1)+myfunc(self,nums,S+nums[idx],idx+1)
            return self.lib[idx][S]
            
        return myfunc(self,nums,S,0)
