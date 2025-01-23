class Solution {
public:
    //  PLEASE LEARN ABOUT CONST USED IN THE FUNCTION DEFINITIONS WHY WE USED AND ALSO INT THE EXCLUDE_LAST PART AND EXCLUDE_FIRST PART WE SLICED THE ARRAYS TRICKLY BY USING THE ACTUAL ARRAY NAM ESTUDY ABOUT THAT ALSO
    int findMaxSum(const vector<int>& arr) {
            // code here
            // TABULATION METHOD
            int prev = arr[0];
            int prev2 = 0;
                //  PLEASE LEARN ABOUT CONST USED IN THE FUNCTION DEFINITIONS WHY WE USED AND ALSO INT THE EXCLUDE_LAST PART AND EXCLUDE_FIRST PART WE SLICED THE ARRAYS TRICKLY BY USING THE ACTUAL ARRAY NAM ESTUDY ABOUT THAT ALSO
            for(int i=1;i<arr.size();i++)
            {
                int pick = arr[i] + prev2;
                int non_pick = prev;
                int current = max(pick,non_pick);
                prev2 = prev;
                prev = current;
                
            }
            
            return prev;
            
        }
    //  PLEASE LEARN ABOUT CONST USED IN THE FUNCTION DEFINITIONS WHY WE USED AND ALSO INT THE EXCLUDE_LAST PART AND EXCLUDE_FIRST PART WE SLICED THE ARRAYS TRICKLY BY USING THE ACTUAL ARRAY NAM ESTUDY ABOUT THAT ALSO
    int rob(const vector<int>& arr) {
        if(arr.size() == 1)
        {
            return arr[0];
        }
        if(arr.size() == 2){
            return max(arr[0],arr[1]);
        }
            //  PLEASE LEARN ABOUT CONST USED IN THE FUNCTION DEFINITIONS WHY WE USED AND ALSO INT THE EXCLUDE_LAST PART AND EXCLUDE_FIRST PART WE SLICED THE ARRAYS TRICKLY BY USING THE ACTUAL ARRAY NAM ESTUDY ABOUT THAT ALSO
    int exclude_last = findMaxSum(vector<int>(arr.begin(), arr.end() - 1));
    int exclude_first = findMaxSum(vector<int>(arr.begin() + 1, arr.end()));

    return max(exclude_first,exclude_last);
        //  PLEASE LEARN ABOUT CONST USED IN THE FUNCTION DEFINITIONS WHY WE USED AND ALSO INT THE EXCLUDE_LAST PART AND EXCLUDE_FIRST PART WE SLICED THE ARRAYS TRICKLY BY USING THE ACTUAL ARRAY NAM ESTUDY ABOUT THAT ALSO
        
    }
};