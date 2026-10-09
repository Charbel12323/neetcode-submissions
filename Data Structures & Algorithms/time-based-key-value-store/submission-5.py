class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # So a key contains multiple values
        # Each value has a corresponding timestamp
        # They are stored in ascending order
        # Therefore to find the value of that timestamp
        # We can use binary search to quickly figure that out
        values = self.store[key]

        left, right = 0, len(values) - 1

        while left <= right:
            middle = (left + right) // 2

            val, time = values[middle]

            if time > timestamp:
                right = middle - 1
            elif time < timestamp:
                left = middle + 1
            else:
                return val
        
        if right >= 0:
            return values[right][0]
        
        return ""
        
