#there is something wrong with this version

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        NN=[nums]
        
        def myfunc(NN):
            #print(NN)
            if len(NN[0])==1:
                return NN
            
            NewNN= []
            for i in range(len(NN)):
                data=NN[i].copy()
                first=data.pop(0)
                print(first)
                tmp=myfunc([data])
                for j in range(len(tmp)):
                    NewNN.append(tmp[j]+[first])
                    NewNN.append([first]+tmp[j])
            return NewNN
        
        return myfunc(NN)
