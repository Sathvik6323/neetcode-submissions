class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        # If s1 is longer than s2, s2 cannot contain a permutation
        if n1 > n2:
            return False
            
        hashset = {}
        
        # 1. Initialize the first window
        # We 'add' counts for s1 and 'subtract' counts for the first window of s2
        for i in range(n1):
            hashset[s1[i]] = hashset.get(s1[i], 0) + 1
            hashset[s2[i]] = hashset.get(s2[i], 0) - 1
            
        # If all counts are 0, the first n1 characters of s2 are a permutation
        if all(v == 0 for v in hashset.values()):
            return True
            
        # 2. Slide the window across s2
        # i represents the index of the character entering the window
        for i in range(n1, n2):
            in_char = s2[i]
            out_char = s2[i - n1]
            
            # The character entering the window: decrease its count
            hashset[in_char] = hashset.get(in_char, 0) - 1
            # The character leaving the window: increase its count back
            hashset[out_char] = hashset.get(out_char, 0) + 1
            
            # Check if current window is a match
            if all(v == 0 for v in hashset.values()):
                return True
                
        return False