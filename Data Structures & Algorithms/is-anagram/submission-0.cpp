class Solution {
public:
    bool isAnagram(string s, string t) {
        int n=s.size();
        int m=t.size();
        if(n!=m){
            return false;
        }
        int s1[26]={0};

        for(int i=0;i<n;i++){
            s1[s[i]-'a']++;
            s1[t[i]-'a']--;
        }
        for(int i=0;i<26;i++){
            if(s1[i]!=0){
                return false;
            }               
            }
        return true;

    }
};
