#there is something wrong with <myfunc>
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        NN=[nums]
        
        def myfunc2(NN):
            NewNN=[]
 #           print(NN)
            if len(NN[0])==1:
                return NN
            
            
            for i in range(len(NN)):
                for j in range(len(NN[i])):
                    data=NN[i].copy()
                    first = data.pop(j)
                    tmp = myfunc2([data])
                    for jj in range(len(tmp)):
                        NewNN.append([first]+tmp[jj])
                        
            return NewNN
        
        
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
                print(NewNN)
            return NewNN
        
        return myfunc2(NN)
