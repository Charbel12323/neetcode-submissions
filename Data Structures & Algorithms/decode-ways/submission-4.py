class Solution:
    def numDecodings(self, s: str) -> int:
        results = {} # for each index -> total number of ways
        def dfs(i):
            if i in results:
                return results[i]

            if i < 0:
                return 1

            numberOfWays = 0

            # Choice 1: Decode current digit individually
            if '1' <= s[i] <= '9':
                numberOfWays += dfs(i - 1)

            # Choice 2: Decode previous + current digit
            if i >= 1 and 10 <= int(s[i-1:i+1]) <= 26:
                numberOfWays += dfs(i - 2)
            
            results[i] = numberOfWays
            
            return numberOfWays

        return dfs(len(s) - 1)


        # number of ways to decode nothing is 0
        # we know the number of ways to decode a single number is 1
        
        prev1 = 1
        prev2 = 0

        for i in range(2, len(s)):
            temp = prev1

            if '1' <= s[i] <= '9':
                prev1 += 1
            
            if '10' <= s[i-1:i+1] <= '26':
                prev1 += 1
            
            prev2 = temp

        
        return prev1
