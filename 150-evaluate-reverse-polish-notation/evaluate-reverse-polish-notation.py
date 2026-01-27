class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {
            "+" : lambda a , b :a+b ,
             "-" : lambda a , b :a - b ,
              "*" : lambda a , b :a *b ,
               "/" : lambda a , b :int(a/b )
        }
        for i in tokens:
            if i in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[i](b, a))
            else:
                stack.append(int(i))

        return stack[0]