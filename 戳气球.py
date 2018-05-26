#为何加个hashtable就错了呢？？？？？
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        def sortedjoin(num_list):
            num_list.sort()     
            return "".join(str(x) for x in num_list)
        
        
        
        self.lib={}
        
        def myfunc(self,nums,bursted_list):            
            
            if len(bursted_list)!=0:
                key = sortedjoin(bursted_list)
                if key in self.lib:
                    print('key',key,self.lib[key])
 #                   return self.lib[key]
            
            
            if len(nums)==1:
                return nums[0]
 #           if len(nums)==2:
 #               return max[nums[0]+nums[0]*nums[1]
            
            count=0
            rec=[]
            for i in range(len(nums)):
                tmp=nums.copy()
                if i==0:
                    cur_coin = tmp[i]*tmp[i+1]
                elif i==(len(nums)-1):
                    cur_coin = tmp[i]*tmp[i-1]
                else:
                    cur_coin = tmp[i]*tmp[i-1]*tmp[i+1]
                tmp.pop(i)
                rec=rec+[myfunc(self,tmp,bursted_list+[i])+cur_coin]
 #           print(rec)
            count = max(rec)
            
            if len(bursted_list)!=0:
                key = sortedjoin(bursted_list)
 #               if key in self.lib:
#                    print (key, self.lib[key],count)
                self.lib[key]=count
                #print(self.lib)
                print('new',key,count)
    
            return count
        
        return myfunc(self,nums,[])
#ver 1, too slow
class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        
        
        def myfunc(self,nums):            
            
            if len(nums)==1:
                return nums[0]
 #           if len(nums)==2:
 #               return max[nums[0]+nums[0]*nums[1]
            
            count=0
            rec=[]
            for i in range(len(nums)):
                tmp=nums.copy()
                if i==0:
                    cur_coin = tmp[i]*tmp[i+1]
                elif i==(len(nums)-1):
                    cur_coin = tmp[i]*tmp[i-1]
                else:
                    cur_coin = tmp[i]*tmp[i-1]*tmp[i+1]
                tmp.pop(i)
                rec=rec+[myfunc(self,tmp)+cur_coin]
 #           print(rec)
            count = max(rec)
            return count
        
        return myfunc(self,nums)
