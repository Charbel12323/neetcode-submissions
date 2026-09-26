from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)

        for first in sorted(count):
            if count[first] > 0:
                amount = count[first]

                for card in range(first, first + groupSize):
                    if count[card] < amount:
                        return False

                    count[card] -= amount

        return True