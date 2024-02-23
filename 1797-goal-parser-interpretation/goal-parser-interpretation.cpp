class Solution {
public:
    string interpret(string command) {
        int i=0;
        string s;
        while(i<command.size())
        {
            if(command[i]=='(' && command[i+1]==')')
            {
             s=s+'o';
             i=i+2;   
            }
            else if(command[i]=='(' && command[i+1]=='a')
            {
                s=s+"al";
                i=i+4;
            }
            else if(command[i]=='G')
            {
                s=s+'G';
                i=i+1;
            }
        else
        {
            i=i+1;
        }
        }
        // if(i==command.size()-1 && command[i]=='G');
        // {
        //     s=s+command[i];
        // }
    return s;
    }
};