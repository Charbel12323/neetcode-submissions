class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        results = []

        # Are these intervals sorted -> No
        # Brute force solution
        # FOr every interval, i'd first compare with all the other intervals and ensure that the array is sorted
        # Thats going to be O(n^2)
        # Instead I can use .sort which is nlogn and then merge them in O(n) time whhich would lead toao c=time complexity of O(nlogn)

        intervals.sort()

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > results[-1][1]:
                results.append(intervals[i])
            else:
                results[-1][1] = max(intervals[i][1], results[-1][1])
        
        
        return results

