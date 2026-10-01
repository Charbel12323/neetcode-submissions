class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        results = []
        path = []
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(index):
            if len(path) == len(digits):
                results.append("".join(path))
                return
            
            letters = phone[digits[index]]

            for letter in letters:
                path.append(letter)
                backtrack(index + 1)
                path.pop()
            
        backtrack(0)
        return results


