class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stk = []

        for oper in operations:
            if oper.isdigit() or oper[0] == '-':
                stk.append(int(oper))
            elif oper == '+':
                stk.append(stk[-1] + stk[-2])
            elif oper == 'D':
                stk.append(stk[-1] * 2)
            elif oper == 'C':
                stk.pop()

        return sum(stk)
