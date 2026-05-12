class PrefixTree:

    def __init__(self):
        self.t = {}

    def insert(self, word: str) -> None:
        temp = self.t
        for w in word:
            if w not in temp:
                temp[w] = dict()
            temp = temp[w]
        temp['\\'] = None

    def search(self, word: str) -> bool:
        temp = self.t
        for w in word:
            if w not in temp: return False
            temp = temp[w]
        return True if "\\" in temp else False

    def startsWith(self, prefix: str) -> bool:
        temp = self.t
        for p in prefix:
            if p not in temp: return False
            temp = temp[p]
        return True