from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I am given a list of integer nums, you would like me to return the k most frequent numbers

        # 1,2,2,3,3,3 and k = 2 you wuold like mt o return 2 and 3

        # Askign about input and output
        # can the input be empty - No
        # Can there be more distinc elemnts than k - No
        # What if all the distinc elements have the same frequencies?
        # Are there negative values? Yes
        
        # We want the top k greatest countso we could use a min heap to store the count and its respective value.
        # So for every value we get the its occurance and add it to the min heap and we must keep the size of the min heap < k
        # Were looping through the list of nums, for each number we increment its count and add it to the min heap.
        # So O(n . logk) equal to nlogk but if k is equal the length of n we can get nlogn
        # A more optimal solution is to get the count of each disting element
        # then we build a bucket where each index repersts a frequency.
        #  1, 2, 3
        # then we just loop from the back of the array which is O(n) so O(n) + O(n) = O(n)

        count = defaultdict(list)
        count = Counter(nums)

        frequency_bucket = [[] for _ in range(len(nums) + 1)]

        for value, freq in count.items():
            frequency_bucket[freq].append(value)
        
        results = []
        for i in range(len(nums), -1, -1):
            for val in frequency_bucket[i]:
                results.append(val)
                if len(results) == k:
                    return results

        
