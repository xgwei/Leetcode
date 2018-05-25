class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        if len(A)<3:
            return 0
        
        #Adif=A[1:]-A[0:-1]
        #Adiff=Adif[1:]-Adif[0:-1]
        
        Adiff=[0 for i in range(len(A)-2)]
        for i in range(len(A)-2):
            Adiff[i]=(A[i+1]-A[i])-(A[i+2]-A[i+1])
        
        print(Adiff)
        rec=[]
        tmp=0
        sig=0
        for i in range(len(Adiff)):
            if Adiff[i]==0:
                sig=1
                tmp=tmp+1
            if Adiff[i]!=0:
                if sig==1:
                    rec=rec+[tmp]
                    tmp=0
                sig=0
            if i==(len(Adiff)-1):
 #               print(sig, tmp)
                if sig==1:
                    rec=rec+[tmp]
        if len(rec)==0:
            return 0
        
        print(rec)
        lib={}
        for i in range(1,max(rec)+1):
            lib[i]=i*(i+1)/2
        
        output=0
        for i in rec:
            output = output+lib[i]
        
        return int(output)
