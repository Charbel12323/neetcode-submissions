class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # The most frequent element is going to be the length of the array
        # If we have 6 elements the highest frequency is going to be 6
        # If we use a hashmap we can get the count of each element but then we would need to add extra logic to figure out what the k most frequent elements are

        # What we can rather do is create frequency buckets from 0 -> len(nums)
        # and just reverse the order until you reach k on the right most side

        frequency = [[] for _ in range(len(nums) + 1)]

        seen = defaultdict(int) # Maps the integer value to its count

        for num in nums:
            seen[num] += 1
        
        # We know have the count of each number its time to put it in the frequency bucket

        for num, count in seen.items():
            frequency[count].append(num)
        
        result = []
        for count in range(len(nums), 0, -1):
            for num in frequency[count]:
                result.append(num)
                if len(result) == k:
                    return result

