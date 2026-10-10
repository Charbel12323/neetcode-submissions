class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute force solution - For each index I would loop through the other index getting the max_frequency and checking repplacements = window size - max_frequency 

        # Optimal solution - Loop through the string once for each character I check if its equal to the one before if it is then we could keep goign updating the max_frequency. replacements = window_size - max_freq = replacements

        # I am given a string s
        # and an interger k
        # You would like me to get the longest repeating characters
        # I can get up to k additions
        
        count = {}
        max_frequency = 0
        max_length = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            while (right - left + 1) - max_frequency > k:
                count[s[left]] -= 1
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length


        





            
            

        