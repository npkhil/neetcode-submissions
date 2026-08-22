class TimeMap:

    def __init__(self):
        self.data = defaultdict(dict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        times = list(self.data[key].keys())
        l = 0
        r = len(times) - 1
        while l <= r:
            c = (l + r) // 2
            if times[c] < timestamp:
                l = c + 1
            elif times[c] > timestamp:
                r = c - 1
            else:
                return self.data[key][times[c]]
        if l == 0:
            return ""
        return self.data[key][times[l - 1]]
