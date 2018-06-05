class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list=str.split()
        
        if len(str_list)!=len(pattern):
            return False
        
        lib_forward={}
        lib_backward={}
        for i in range(len(str_list)):
#            print(lib)
            if str_list[i] not in lib_forward:
                lib_forward[str_list[i]]=pattern[i]
            if pattern[i] not in lib_backward:
                lib_backward[pattern[i]]=str_list[i]
            if (pattern[i]!=lib_forward[str_list[i]])|(str_list[i]!=lib_backward[pattern[i]]):
                return False
                    
        return True
