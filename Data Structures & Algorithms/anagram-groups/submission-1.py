class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # So we have the same characters - we can use the count in a hash mpa
        # order doesnt matter

        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for ch in s:
                count[ord(ch) - ord('a')] += 1
            
            anagram_map[tuple(count)].append(s)
        
        return list(anagram_map.values())