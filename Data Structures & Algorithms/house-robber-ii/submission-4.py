class Solution:
    def rob(self, nums: List[int]) -> int:
        # We are going to split nums into two arrays inclduing beginning, exluding beginning
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        include_beginning = nums[:-1]
        exlude_beginning = nums[1:]

        first_amount = self.calculate_amount(include_beginning)
        end_amount = self.calculate_amount(exlude_beginning)

        return max(first_amount, end_amount)

    def calculate_amount(self,array_split):
        prev1 = max(array_split[0], array_split[1])
        prev2 = array_split[0]
        current = 0
        for i in range(2, len(array_split)):
            current = max(prev1, prev2 + array_split[i])

            prev2 = prev1
            prev1 = current
        
        return prev1
