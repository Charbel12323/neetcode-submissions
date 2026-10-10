class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # We know we have a fixed size window of s1. What we can do is getting the count of character up to the size of the window#
        # Once we reach that size, we can easily check if the count matches, if it doesn't then we must erase the left count and do left += 1

        count_s1 = Counter(s1)

        left = 0
        count_s2 = {}
        for right in range(len(s2)):
            count_s2[s2[right]] = count_s2.get(s2[right],0) + 1

            if (right - left + 1) == len(s1):
                if count_s2 == count_s1:
                    return True
                
                count_s2[s2[left]] -= 1
                if count_s2[s2[left]] == 0:
                    del count_s2[s2[left]]
                
                left += 1
        
        return False
