class Solution {
public:
    int possibleStringCount(string word) {
        int count = 1;
        for(char i=0;i<word.size();i++){
            if(word[i] == word[i+1]){
                count++;
            }
        }
        return count;
    }
};