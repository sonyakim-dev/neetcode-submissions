class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ']':
                temp = ''
                while stk[-1] != '[':
                    temp += stk.pop()

                stk.pop() # pop '['
                
                count = ''
                while stk and stk[-1].isdigit():
                    count += stk.pop()

                for _ in range(int(count[::-1])):
                    stk.extend(temp[::-1])
            else:
                stk.append(c)

        return ''.join(stk)