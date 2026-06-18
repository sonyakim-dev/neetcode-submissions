class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = defaultdict(list) # key: sorted str, val: list of strs
        for s in strs:
            ana["".join(sorted(s))].append(s)
        return list(ana.values())