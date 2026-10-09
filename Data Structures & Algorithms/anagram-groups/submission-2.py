class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n^2 x K)
        # So we can use a hashmap to store the count of the string
        # Then for every other string we do the same if that count which is the key exists we append it if not we create a new one

        # O(n.k) space = O(n)

        # if empty return [""]
        # if there is only one string we just return that
        
        if len(strs) == 1:
            return [strs]
        
        anagram_map = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch) - ord('a')] += 1
            
            anagram_map[tuple(count)].append(word)
        
        return list(anagram_map.values())