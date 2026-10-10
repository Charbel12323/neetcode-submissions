class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we have odd and even substrings so we must check both
        # for even substrings we would need to have 2 pointers next to each other
        # but for odd we can have them starting at the same character

        longest_substring = ""

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:

                if (right - left + 1) > len(longest_substring):
                    longest_substring = s[left: right + 1]
                
                left -= 1
                right += 1
            
            left = i
            right = i + 1

            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                if (right - left + 1) > len(longest_substring):
                    longest_substring = s[left:right + 1]

                left -= 1
                right += 1
        
        return longest_substring


