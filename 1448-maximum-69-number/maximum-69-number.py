class Solution(object):
    def maximum69Number (self, num):
        strnum = str(num)
        res = ''
        for i in strnum:
            if i == "6":
                strnum = strnum.replace("6","9",1)
                break
           
        return int(strnum)
        
        