class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.store = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.values) - 1
        res = ""

        while l <= r:
            mid = l + ((r - l)) // 2

            time = values[mid][0]

            if time <= timestamp:
                res = values[mid][1]
                l = mid + 1
            else:
                r = m - 1

        return res
