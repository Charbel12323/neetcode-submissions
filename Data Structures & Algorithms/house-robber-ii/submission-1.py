class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(houses):
            n = len(houses)

            if n == 1:
                return houses[0]

            dp = [0] * n

            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i - 2] + houses[i],
                    dp[i - 1]
                )

            return dp[n - 1]

        return max(
            robLinear(nums[:-1]),  # exclude last
            robLinear(nums[1:])    # exclude first
        )