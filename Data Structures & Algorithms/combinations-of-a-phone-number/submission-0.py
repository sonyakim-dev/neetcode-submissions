class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_pad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []


        def dfs(i, fixed):
            if len(fixed) == len(digits):
                result.append(fixed)
                return
            for c in num_pad[digits[i]]:
                dfs(i+1, fixed + c)

        if digits: dfs(0, "")
        return result