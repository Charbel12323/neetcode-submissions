class Solution:

    # Can the input be empty - Yes
    # If the input is empty what should we return -> [""]
    # If the input contains one string we return -> ["String"]
    # WHen encoding it becomes "HELLOWORLD" decode brings it back to ["HELLO", "WORLD"]
    # We need to keep track of the count
    # We need to figure out when to stop counting so we can use some sort of special character "#"
    # Hello, world becomes 5#Hello5#World
    #
    def encode(self, strs: List[str]) -> str:
        results = ""

        for s in strs:
            results += str(len(s)) + "#" + s # 5#Hello5#World
        
        return results

    def decode(self, s: str) -> List[str]:

        i = 0
        results = []
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            results.append(s[start:end])

            i = end
        
        return results
