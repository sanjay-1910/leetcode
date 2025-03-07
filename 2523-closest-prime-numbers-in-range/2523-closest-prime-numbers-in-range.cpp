class Solution {
public:
    vector<int> closestPrimes(int lefto, int righto) {
    int n=righto;
    vector<bool>san(n+1,true);
    san[0]=san[1]=false;
    for(int i=2;i<=sqrt(n);i++)
    {
        if(san[i]) {
            for(int j=i*i;j<n+1;j+=i)
            {
                san[j]=false;
            }
        }
    }
    int left = -1, right = -1, diff = -1, last_prime = -1;  
    for (int j = lefto; j <= righto; j++) {
        if (san[j]) {
            if (left == -1) {
                left = j;
                last_prime = j;
            } else if (right == -1) {
                last_prime = j;
                diff = j - left;
                right = j;
            } else {
                if ((j - last_prime) < diff) {
                    left = last_prime;
                    right = j;
                    diff = j - last_prime;
                }
                last_prime = j;
            }
        }
    }
    if (left != -1 && right != -1) {
        return {left, right};
    } else {
        return {-1, -1};
}
    }
};