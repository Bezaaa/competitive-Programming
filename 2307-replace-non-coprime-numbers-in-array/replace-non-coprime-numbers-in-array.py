
class Solution(object):
    def replaceNonCoprimes(self, nums):
        """
        find adjacent numbers that are non prime
        while they are still non prime replace them with their LCM else continue
       
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        stack = []
        stack.append(nums[0])
        def are_non_coprime(a, b):
            return gcd(a, b) > 1

        def lcm(a, b):
            return abs(a * b) //gcd(a, b)
        for i in range(1 , len(nums)):
            stack.append(nums[i])
            while len(stack) >=2:
                a = stack[-2]
                b = stack[-1]
                if are_non_coprime(a,b):
                    stack.pop()
                    stack.pop()
                    stack.append(lcm(a,b))

                else:
                    break
            
          

        return stack


        