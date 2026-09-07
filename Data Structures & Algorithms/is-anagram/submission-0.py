class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = defaultdict(int)
        count_t = defaultdict(int)

        for ch in s:
            count_s[ch] += 1
        
        for ch in t:
            count_t[ch] += 1
        
        return count_s == count_t