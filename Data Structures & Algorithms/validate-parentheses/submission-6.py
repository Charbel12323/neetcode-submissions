class Solution:
    def isValid(self, s: str) -> bool:
        closing_to_opening = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }

        brackets = []

        for ch in s:
            if ch in closing_to_opening:
                if not brackets or brackets[-1] != closing_to_opening[ch]:
                    return False
                
                brackets.pop()
            else:
                brackets.append(ch)
        
        return True if len(brackets) == 0 else False