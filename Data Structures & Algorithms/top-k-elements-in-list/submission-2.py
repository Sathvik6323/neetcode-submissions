class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary to store the frequency of each number: {number: count}
        count = {}
        
        # Bucket list where index represents frequency: [ [], [nums with freq 1], [nums with freq 2] ]
        # Size is len(nums) + 1 because a number can appear at most len(nums) times
        freq = [[] for _ in range(len(nums) + 1)]

        # Step 1: Count occurrences of each number
        for n in nums:
            # .get(n, 0) handles the "KeyError" by returning 0 if n is not in the dict yet
            count[n] = 1 + count.get(n, 0)
        
        # Step 2: Map frequencies to the bucket list
        for n, c in count.items():
            freq[c].append(n)

        # Step 3: Iterate backwards through the bucket (highest frequency first)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # Once we have found k elements, return the result immediately
                if len(res) == k:
                    return res