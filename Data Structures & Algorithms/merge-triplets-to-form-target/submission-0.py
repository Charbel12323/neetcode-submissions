class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # Sp we canm have multiple triplets
        # You can either max i and j for one triplet and use it elsewhere
        # Or just keep them as is

        found = [False, False, False]
        
        # If we ahve any triplet that has a greater value than target we cant use to max

        for triplet in triplets:

            if (triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]):
                continue
            
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True
        
        return all(found)