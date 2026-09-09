class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}

        for ch in s1:
            count_s1[ch] = count_s1.get(ch, 0) + 1
        
        left = 0

        for right in range(len(s2)):
            count_s2[s2[right]] = count_s2.get(s2[right], 0 ) + 1

            if (right - left + 1) > len(s1):
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]
                left += 1
            
            if count_s1 == count_s2:
                return True
        
        return False