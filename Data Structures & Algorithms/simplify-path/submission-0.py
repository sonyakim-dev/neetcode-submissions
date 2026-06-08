class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        l = 0

        for s in re.split('/', path):
            if not s or s == '.':
                continue
            elif s == '..':
                if stk: stk.pop()
            else:
                stk.append(s)

        return '/' + '/'.join(stk)