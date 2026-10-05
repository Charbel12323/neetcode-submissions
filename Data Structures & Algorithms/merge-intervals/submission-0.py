class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: interval[0])

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            previous = results[-1]
            current = intervals[i]

            # Check 1: completely separate
            if previous[1] < current[0]:
                results.append(current)

            # Otherwise they overlap
            else:
                previous[1] = max(previous[1], current[1])

        return results