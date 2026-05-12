class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in ["(", "[", "{"]:
                stack.append(p)
            elif len(stack) == 0:
                return False
            elif (p == ")" and stack[-1] == "(")\
                or (p == "]" and stack[-1] == "[")\
                or (p == "}" and stack[-1] == "{"):
                stack.pop()
            else:
                return False
        return True if len(stack) == 0 else False