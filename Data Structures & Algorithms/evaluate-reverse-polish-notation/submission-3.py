class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for char in tokens:
            if char not in {'+','-','*','/'}:
                stack.append(char)
            else:
                n2= stack.pop()
                n1=stack.pop()
                if char=="*":
                    res=int(n1)*int(n2)
                    stack.append(res)
                elif char=="+":
                    res=int(n1)+int(n2)
                    stack.append(res)
                elif char=="-":
                    res=int(n1)-int(n2)
                    stack.append(res)
                else:
                    res=int(n1)/int(n2)
                    stack.append(res)
        return int(stack[-1])


        