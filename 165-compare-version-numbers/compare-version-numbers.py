class Solution(object):
    def compareVersion(self, version1, version2):
        v1_list = version1.split('.')
        v2_list = version2.split('.')
        if len(v2_list) < len(v1_list):
            v2_list += [0] * (len(v1_list) - len(v2_list))
        if len(v1_list) < len(v2_list):
            v1_list += [0] * (len(v2_list) - len(v1_list))
        i=0
        while i < len(v1_list):
            if int(v1_list[i]) < int(v2_list[i]):
                return -1
            if int(v1_list[i]) > int(v2_list[i]):
                return 1
            i+=1
        return 0
            

       
        