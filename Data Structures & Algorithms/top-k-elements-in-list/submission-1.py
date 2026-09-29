class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force O(n^2)
        # Optimal solution - We loop through the array once getting the frequency of each element
        # We then create buckets where each index is the frequency and we start at the bottom

        # Example - [1,2,2,3,3,3] 6 5 4 3 2 1
        # Each bucket can contain multiple values since if we have [2,2,2,3,3,3] gives us a fequency of 3 and 3

        count = defaultdict()
        count = Counter(nums) # 1 : 1, 2: 2, 3:3 Value -> frequency

        frequency = [[] for _ in range(len(nums) + 1)]

        for value, freq in count.items():
            frequency[freq].append(value)
        
        result = []
        for i in range(len(frequency) - 1, -1, -1):
            for val in frequency[i]:
                result.append(val)
                if len(result) == k:
                    return result
            
