class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) 
    {
        string ret="";
        int sp=0;
        for (int i=0;i<s.size();i++)
        {
            if (sp<spaces.size() && i==spaces[sp])
            {
                ret.push_back(' ');
                sp++;
            }
            ret.push_back(s[i]);
        }
        return ret;
    }
};