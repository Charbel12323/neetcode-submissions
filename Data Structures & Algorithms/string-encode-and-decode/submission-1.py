class Solution:

    def encode(self, strs: List[str]) -> str:
        # We need to make a list of strings into one string
        # We need to find a way to diffrentiate the words
        # For example:
        # HelloWorld -> We need to know how long the string is to know where to stop, and if it is 2 digits we need to make sure we dont only read 1 so therefore we need a #
        # #5Hello#5World
        # We start with the length and then use # to start counting the characters

        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s
        
        return result

    def decode(self, s: str) -> List[str]:

        result = []
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
