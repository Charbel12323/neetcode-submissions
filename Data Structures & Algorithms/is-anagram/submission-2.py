from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Can either of the inputs be empty - No
        # Are inputs always the same length
        # Return True if yes else no

        # Brut eforce solution is have a pointer at s and t get the coutn of s then run anotehr loop to get the count of t and check. This would be O(n^2) space would be O(1)
        # POptimal solution. I can have a hashmap storing both counts of each string
        # If they are equal then we are good if not then return False
        # Time complexity wold be O(n) space would be O(n)

        # Implementation logic
        # If we len(s) != len(t) then we can immediately return False
        # we can create 2 hashmaps count_1 and count_2
        # The key will be the letter and valu will be the count
        # This would be O(n) time and space

        if len(s) != len(t):
            return False
        
        count_1 = {}
        count_2 = {}

        count_1 = Counter(s) # O(n)
        count_2 = Counter(t) # O(n)

        if count_1 == count_2:
            return True
        
        return False

        

