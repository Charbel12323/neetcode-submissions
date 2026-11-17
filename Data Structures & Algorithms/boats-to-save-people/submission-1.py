class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        Each index represents a weight of the ith person
        Infinite number of boats
        Each boat can carry a weight limit
        Each boat can hold at most two people

        Return the minimum number of boats to carry every given person


        1) Can the length of the array be less than 2
        2) Is there always a valid solution - Yes limit is always going to be <= to people

        The boats dont have to be in consecutive order

        Brute force
        For each boat, if the weight is less than the limit we are going to have a pointer that iterates through all other boats and adds one of them if its less than or equal to limit then we are good
        We do the same thing over and over again
        Time complexity = O(n^2)
        Space complexity = O(1)


        """

        people.sort()
        numberOfBoats = 0

        left, right = 0, len(people) - 1

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
               

            numberOfBoats += 1
            right -= 1
        
        return numberOfBoats

