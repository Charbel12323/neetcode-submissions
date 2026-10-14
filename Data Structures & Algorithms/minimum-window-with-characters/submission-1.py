class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # We can get the count of t
        # We can iterate through the sunstring s
        # until all the characters in t including duplicates exist in s
        # Once this condition is True
        # We can slice the vlaue using left and right pointers
        # And store that results
        # We can then shorten the substring until the condition is no longer True
        # Once that condition is no longer true, we can then keep increaseing the size of the window until it is again. And we keep doing that until wepass the lass character in s
        # THen we can just return that substring

        # O(N + T) O(N + T)
        # length of t can be greater than s
        # If thats the case return ""
        
        if len(t) > len(s):
            return ""
        
        count_t = Counter(t) # O(n) {ch: freq}

        shortest_substring = ""
        shortest_size = float('inf')
        count_s = defaultdict(int)
        have = 0 # Number of characters that match t
        need = len(count_t)

        left = 0

        for right in range(len(s)):
            ch = s[right]
            count_s[ch] = count_s.get(ch, 0) + 1

            if ch in count_t:
                if count_s[ch] == count_t[ch]:
                    have += 1
            
            while have == need :
                if (right - left + 1) < shortest_size:

                    shortest_substring = s[left : right + 1]
                    shortest_size = right - left + 1
                
                count_s[s[left]] -= 1

                if s[left] in count_t:
                    if count_s[s[left]] < count_t[s[left]]:
                        have -= 1
                
                left += 1
            
        return shortest_substring