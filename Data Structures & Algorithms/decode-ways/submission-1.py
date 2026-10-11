class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev2 = 1  # Ways to decode empty prefix
        prev1 = 1  # Ways to decode first character

        for i in range(1, len(s)):
            current = 0

            # Option 1: Decode current digit alone
            if s[i] != "0":
                current += prev1

            # Option 2: Decode previous two digits together
            if 10 <= int(s[i-1:i+1]) <= 26:
                current += prev2

            prev2 = prev1
            prev1 = current

        return prev1