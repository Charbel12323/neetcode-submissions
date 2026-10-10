class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Brute Force
        # - For each index, i'd loop all the other index and store the max_count found

        # O(n^2)

        # Optimal solution
        # we go through every character if a character has been seen we get the max_count increment the lef tpointer and remove it from teh store

        seen = {} # Value : count
        left = 0
        max_count = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen[s[left]] -= 1
                if seen[s[left]] == 0:
                    del seen[s[left]]
                
                left += 1
            
            seen[s[right]] = seen.get(s[right], 0 ) + 1
            max_count = max(max_count, right - left + 1)
        
        return max_count



