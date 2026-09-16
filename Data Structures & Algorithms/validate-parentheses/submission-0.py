class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        closing_to_opening = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        for ch in s:
            if ch not in closing_to_opening:
                brackets.append(ch)
            else:
                if not brackets:
                    return False
                
                opening = brackets.pop()

                if opening != closing_to_opening[ch]:
                    return False
        
        return len(brackets) == 0
