class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        lst = self.data[key]
        l, r = 0, len(lst) - 1
        result = ''
        while l <= r:
            m = (l + r) // 2
            if lst[m][1] <= timestamp:
                result = lst[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
