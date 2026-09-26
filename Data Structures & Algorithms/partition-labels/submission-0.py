class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = Counter(s)

        seen = set()
        result = []
        count_substring = 0
        for ch in s:
            if ch not in seen:
                seen.add(ch)
            
            count[ch] -= 1
            count_substring += 1

            if count[ch] == 0:
                del count[ch]
                seen.remove(ch)
            
            if not seen:
                result.append(count_substring)
                count_substring = 0
        
        return result

            
