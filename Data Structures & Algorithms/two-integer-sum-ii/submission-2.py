class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # is there always a unique solution? If not what should I return
        # Can numbers be empty
        # Can numbers contain negative values
        # the output should be an array correct

        # Example, if we have [1,2,3,4] and target = 3
        # 1 + 2 = 3 so I should return [1,2]. Return the non 0 index

        # Brute force solution:
        # We can use a hashmap where the key is the value and the value is the index.
        # We can check if the composite exists if it does we return the composite is index since it was first and then the current index
        # This would be O(n) for both space and time since we are looping through all the nums and storing nums in the set so O(n) space is occupied


        # The more optimal solution: 
        # We can have 2 pointers. Since it is sorted, we can have one pointer on the left and one pointer on the right. We do right + left. If it is greater than value then we move right to the left to decrease the total sum. Vice verse, if we add and its too small we move to the left. 

        # Since we cant use the same index twice we need to ensure left is always less than right

        left, right = 0, len(numbers) - 1

        while left < right:

            total = numbers[left] + numbers[right]

            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
        
        # Since there is always a unique solution we dont need ot return anything here
