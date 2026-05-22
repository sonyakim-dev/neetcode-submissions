class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        3 -> d
          -> e
          -> f
        """
        num_pad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",\
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        
        def dfs(i, fixed):
            if i >= len(digits):
                if fixed: result.append(fixed)
                return
            for alpha in num_pad[digits[i]]:
                dfs(i+1, fixed + alpha)

        dfs(0, "")
        return result