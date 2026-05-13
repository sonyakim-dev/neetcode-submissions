class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == '+':
                nums.append(nums.pop() + nums.pop())
            elif t == '-':
                n2, n1 = nums.pop(), nums.pop()
                nums.append(n1 - n2)
            elif t == '*':
                nums.append(nums.pop() * nums.pop())
            elif t == '/':
                n2, n1 = nums.pop(), nums.pop()
                nums.append(int(float(n1) / n2))
            else:
                nums.append(int(t))
            
        return nums[0]
