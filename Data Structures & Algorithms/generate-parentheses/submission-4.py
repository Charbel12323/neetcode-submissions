class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We are given n = 1, we need to have one open and one closed parantheses
        # We are given n = 3, 3 open and 3 closed
        # "()()()", "((()))"
        # Ordering matters
        # By the end u need 3 opening and closing
        #  ()) Cant add a closing if there is less opening
        # Only you can adding openings because in they in the end they can be closed
        
        open_bracket = 0
        closing_brackets = 0
        results = []
        path = []

        def backtrack(opening, closing):
            if opening == closing and opening == n:
                results.append("".join(path))
                return
            
            if opening < n:
                path.append("(")
                backtrack(opening + 1, closing)
                path.pop()
            
            if closing < opening:
                path.append(")")
                backtrack(opening, closing + 1)
                path.pop()
        
        backtrack(0,0)
        return results