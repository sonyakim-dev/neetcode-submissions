class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {")": "(", "]": "[", "}": "{"}

        for p in s:
            if p in "([{":
                stack.append(p)
            elif len(stack) > 0 and pair[p] == stack[-1]:
                stack.pop()
            else:
                return False
                
        return True if len(stack) == 0 else False