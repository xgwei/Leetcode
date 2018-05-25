class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
#        grid=numpy.asarray(grid)
#        print(grid)
        
#        def partial_listMatrix(X,i_start,i_end,j_start,j_end)
        
    
        self.lib={}
        for i in range(len(grid)):
            self.lib[i]={}
            for j in range(len(grid[0])):
                self.lib[i][j]=False
            
        print(self.lib)
        
        def myfunc(self,grid,i_end,j_end):
 #           global lib
  #          print(self.lib)
            if self.lib[i_end][j_end]:
                return self.lib[i_end][j_end]
                
            if (i_end==0)&(j_end==0):
                self.lib[i_end][j_end]=grid[0][0]
                return grid[0][0]
            if (i_end==0)&(j_end==1):
                self.lib[i_end][j_end]=grid[0][0]+grid[0][1]
                return grid[0][0]+grid[0][1]
            if (i_end==1)&(j_end==0):
                self.lib[i_end][j_end]=grid[0][0]+grid[1][0]
                return grid[0][0]+grid[1][0]
            if (i_end==1)&(j_end==1):
                self.lib[i_end][j_end]=min(grid[0][0]+grid[0][1]+grid[1][1],grid[0][0]+grid[1][0]+grid[1][1])
                return min(grid[0][0]+grid[0][1]+grid[1][1],grid[0][0]+grid[1][0]+grid[1][1])
   #         print (grid,i_end,j_end)
            
            if (i_end>0)&(j_end>0):
                tmp=grid[i_end][j_end]+min(myfunc(self,grid,i_end-1,j_end),myfunc(self,grid,i_end,j_end-1))
                self.lib[i_end][j_end]=tmp
                return tmp
            if (i_end==0):
                tmp=grid[i_end][j_end]+myfunc(self,grid,i_end,j_end-1)
                self.lib[i_end][j_end]=tmp
                return tmp
            if (j_end==0):
                tmp=grid[i_end][j_end]+myfunc(self,grid,i_end-1,j_end)
                self.lib[i_end][j_end]=tmp
                return tmp
        
        
        return myfunc(self,grid,len(grid)-1,len(grid[0])-1)
