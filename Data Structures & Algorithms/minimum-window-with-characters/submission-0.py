class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}

        for ch in t:
            count_t[ch] = count_t.get(ch,0) + 1
        
        left = 0
        result = ""
        min_length = float('inf')
        have = 0
        need = len(count_t)
        count_s = {}

        for right in range(len(s)):
            if s[right] in count_t:
                count_s[s[right]] = count_s.get(s[right],0 ) + 1

                if count_s[s[right]] == count_t[s[right]]:
                    have += 1
            
            while have == need:

                if right - left + 1 < min_length:
                    min_length = min(min_length, right - left + 1)
                    result = s[left: right + 1]
                
                if s[left] in count_t:
                    count_s[s[left]] -= 1

                    if count_s[s[left]] < count_t[s[left]]:
                        have -= 1
                
                left += 1
        
        return result

            