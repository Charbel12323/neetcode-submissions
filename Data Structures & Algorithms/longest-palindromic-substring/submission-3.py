class Solution:
    def longestPalindrome(self, s: str) -> str:
        # what is a palindorme
        # A palindrome is a substring that can be reverse and read the same as original
        # so lets assume abba -> reverse -> abba
        # aba -> reverse -> aba
        # dp[i][j] is a boolean of whether the substring s[i:j] is a palindrome or not
        # then we can check if s[i] == s[j] and dp[i][j] == True
        # expand

        # Even strings and odd strings
        # Why do they differ
        # abba abaer
        # left, right
        # abba left = right we ewould get a m mismatch quite easilt a != b
        # so when it is even number left = i and right = i + 1 HOPING THAT THE MIDDLE IS EQUAL
        # BUT IF ITS ODD THEN WE CAN DO LEFT = RIGHT
        
        result = ""

        for i in range(len(s)):

            # Assume we start with odd
            left = right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left: right + 1]) > len(result):
                    result = s[left: right + 1]

                left -= 1
                right += 1
            
            left, right = i, i + 1
            
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if len(s[left: right + 1]) > len(result):
                    result = s[left: right + 1]

                left -= 1
                right += 1
            
        
        return result