class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        Solution1 - For each Character iterate through all the other characters ahead and keep track of the number of characters that dont match the starting character.
        Once we reach not_found == k we keep track of the longest substring and then compare it with the current maximum

        Time Complexity O(n^2) since we are process each character more than once


        Solution2 - For each character keep track of the maximum frequency. We then check if right - left + 1 - max_frequency is less thank k i fit is then we are good if not then we must pop from teh left slide. 










        """

        count = {} # Key -> Character , Value -> frequency
        max_frequency = 0
        max_length = 0
        left = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])

            if ((right - left + 1) - max_frequency) <= k:
                max_length = max(max_length, right - left + 1)
                continue
            else:
                count[s[left]] -= 1
                left += 1
        
        return max_length
