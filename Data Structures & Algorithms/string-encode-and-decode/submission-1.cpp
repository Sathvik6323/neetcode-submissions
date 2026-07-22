class Solution {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        string res; // Initialize an empty string to store the encoded result
        for (const string& s : strs) { // Iterate through each string in the input vector
            // Append the length of the current string followed by '#' and the string itself to the result
            res += to_string(s.size()) + "#" + s;
        }
        return res;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        vector<string> res; // Initialize an empty vector to store the decoded strings
        int i = 0; // Initialize an index to track the current position in the encoded string

        while (i < s.size()) { // Iterate through the encoded string
            // Find the index of the '#' character to determine the length of the next string
            int j = i;
            while (s[j] != '#') {
                j++;
            }

            // Extract the length of the next string from the substring
            int length = stoi(s.substr(i, j - i));

            // Advance the index to the start of the next string
            i = j + 1;

            // Extract the next string using the length and add it to the result vector
            res.push_back(s.substr(i, length));

            // Advance the index to the start of the next encoded string
            i = j + length + 1;
        }
        return res;
    }
};