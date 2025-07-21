class Solution(object):
    def makeFancyString(self, s):
        new_string =''
        for i in range(len(s)):
           
            if len(new_string)>=2 and   new_string[-1] == new_string[-2] ==s[i]:
                continue
            else:
               new_string+=s[i]
        return new_string

       
            
       
        

            
        