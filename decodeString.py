class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return s
        
        strStack = list()
        numStack = list()
        num = 0
        currStr = ""
        
        for i in s:
            if i.isdigit():
                num = num*10 + i - '0'
            elif i == '[':
                numStack.append(num)
                strStack.append(currStr)
                num = 0
            
            elif i == ']':
                multFactor = numStack.pop()
                for i in range(multFactor):
                    newStr = newStr + currStr
                currStr = strStack.pop() + newStr
        
            else:
                currStr = cuttStr + i
        
        return currStr
