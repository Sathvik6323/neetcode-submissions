class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""

        # Dictionary to keep a count of all the unique characters in t
        dict_t = {}
        for char in t:
            dict_t[char] = dict_t.get(char, 0) + 1

        # Number of unique characters in t that need to be present in the window
        required = len(dict_t)
        
        # l, r pointers
        l, r = 0, 0
        
        # formed is used to track how many unique characters in t 
        # are present in the current window in required frequency
        formed = 0
        window_counts = {}

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            # If the frequency of the current character added matches 
            # the desired count in t, increment formed
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'
            while l <= r and formed == required:
                char = s[l]

                # Save the smallest window until now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by the `left` pointer 
                # is no longer a part of the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1    

            r += 1    
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]