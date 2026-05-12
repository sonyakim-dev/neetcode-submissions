class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        record = defaultdict(list) # key: sorted str, val: []

        for s in strs:
            record[''.join(sorted(s))].append(s)

        return list(record.values())