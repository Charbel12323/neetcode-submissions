class TimeMap:

    def __init__(self):
        self.timestamps = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.timestamps[key]
        left, right = 0 , len(values) - 1
        result = ""
        
        while left <= right:
            middle = (left + right) // 2

            value, time = values[middle]

            if time <= timestamp:
                result = value
                left = middle + 1
            else:
                right = middle - 1
        
        return result
        
