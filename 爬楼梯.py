'''
假设你正在爬楼梯。需要 n 步你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 步 + 1 步
2.  2 步
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 步 + 1 步 + 1 步
2.  1 步 + 2 步
3.  2 步 + 1 步

最后一步可以是1步也可以是两步

'''

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 1
        if n==2:
            return 2
        
        a = [1, 2]
        
        for i in range(2,n):
            a.append(a[i-1]+a[i-2])
        return a[-1]
        
        '''
        def climb(n):
            if n==0:
                return 0
            if n==1:
                return 1
            if n==2:
                return 2
            return climb(n-1)+climb(n-2)
        return climb(n)
        '''
