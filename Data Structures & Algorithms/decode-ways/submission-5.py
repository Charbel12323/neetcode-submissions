class Solution:
    def numDecodings(self, s: str) -> int:
        prev2 = 1
        prev1 = 1 if s[0] != '0' else 0

        for i in range(1, len(s)):
            current = 0

            # Decode current digit individually
            if '1' <= s[i] <= '9':
                current += prev1

            # Decode previous + current digit
            if '10' <= s[i-1:i+1] <= '26':
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1