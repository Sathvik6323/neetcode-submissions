class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // Create a hash map to count the frequency of each number
        unordered_map<int, int> cnt;
        // Create a vector of vectors to store numbers by their frequency
        vector<vector<int>> freq(nums.size() + 1);

        // Count the frequency of each number
        for (auto i : nums) {
            cnt[i]++;
        }

        // Group numbers by their frequency
        for (const auto& entry : cnt) {
            freq[entry.second].push_back(entry.first);
        }

        // Iterate through the frequency buckets in descending order
        vector<int> res;
        for (int i = freq.size() - 1; i > 0; --i) {
            // Iterate through the numbers in the current frequency bucket
            for (int n : freq[i]) {
                // Add the number to the result
                res.push_back(n);
                // If we've reached the desired number of top frequent elements, return the result
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};