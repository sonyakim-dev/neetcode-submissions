class Solution:
    def decodeString(self, s: str) -> str:
        curr_str = ''
        str_stk = ['']
        curr_num = 0
        num_stk = []

        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                str_stk.append(curr_str)
                num_stk.append(curr_num)
                curr_str = ''
                curr_num = 0
            elif c == ']':
                temp = str_stk.pop() * num_stk.pop()
                str_stk[-1] = str_stk[-1] + temp
            else: # char
                str_stk[-1] = str_stk[-1] + c

        return ''.join(str_stk)