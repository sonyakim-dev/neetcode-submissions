class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for st in strs:
            ana = "".join(sorted(st))
            result[ana].append(st)
        
        return list(result.values())