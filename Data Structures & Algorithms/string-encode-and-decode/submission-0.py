class Solution:
    # Encoding strings: We must combine all teh strings into one string seperated by something unique.  How do we determine when a string ends. We need the length of the string to encode it. What other scenario are we missing
    def encode(self, strs: List[str]) -> str:
        # As we mentioned need the length and the #
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        5#Hello5#World
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            start = j + 1
            end = start + length
            result.append(s[start:end])

            i = end
        return result
