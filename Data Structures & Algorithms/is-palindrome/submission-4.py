class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Can the input be empty
        # Can the input contain spaces
        # Return True and False
        # We only care about the alphanumeric characters

        # Brute force solution
        # - I'd remove the spaces and special characters
        # - then I'd check teh reverse using a copy 
        # O(n) time and space ( since string has been copied)

        # Optimal solution. I can one pointer on the left, and one pointer on the right. And if both pointers are pointing to a alphanumeric character compare and check if they are equal or not. 

        # This would reduce space complexity to O(1) while keeping time complexit to O(n) since we are still looping through the string

        if len(s) == 1:
            return True
        
        left, right = 0, len(s) - 1

        while left < right:

            while not s[left].isalnum() and left < right:
                left += 1
            
            while not s[right].isalnum() and right > left:
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True
