class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We can use the length of the sliding window subtracted by the maximum frequency character and if that value is less than k then we are good
        """



        frequency_count = defaultdict(int)

        left = 0
        max_freq = 0
        answer = 0
        for right, ch in enumerate(s):
            frequency_count[ch] = frequency_count.get(ch, 0) + 1
            max_freq = max(max_freq, frequency_count[ch])

            if (right - left + 1) - max_freq <= k:
                answer = max(answer, right - left + 1)
                continue
            frequency_count[s[left]] -= 1
            left += 1
        
        return answer
