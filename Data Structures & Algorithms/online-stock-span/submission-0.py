class StockSpanner:
    # [100, 80, 60, 70, 60]
    def __init__(self):
        self.stock = []

    def next(self, price: int) -> int:
        self.stock.append(price)
        count = 0
        for i in range(len(self.stock)-1, -1, -1):
            if self.stock[i] > price:
                return count
            count += 1
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)