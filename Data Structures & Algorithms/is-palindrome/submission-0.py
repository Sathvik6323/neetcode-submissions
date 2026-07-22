class Solution:
    def isPalindrome(self, s: str) -> bool:

        
        s=s.lower()
        s=s.replace(" ","")
        l,r=0, len(s)-1
        while l < r:
            # Skip non-alphanumeric characters from the left
            while l < r and not s[l].isalnum():
                l += 1
            # Skip non-alphanumeric characters from the right
            while r > l and not s[r].isalnum():
                r -= 1
            
            # Compare lowercase versions
            if s[l].lower() != s[r].lower():
                return False
                
            l += 1
            r -= 1
        return True
            