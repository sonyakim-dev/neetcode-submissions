class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(dict) # key

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[timestamp][key] = value

    def get(self, key: str, timestamp: int) -> str:
        for t in range(timestamp, -1, -1):
            if key in self.tmap[t]:
                return self.tmap[t][key]
        return ""
