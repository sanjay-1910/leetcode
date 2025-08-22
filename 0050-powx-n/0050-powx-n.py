class Solution:
    def myPow(self, x: float, n: int) -> float:
        # def po(pow,exp):
        def fastPow(base, exp):
            if exp == 0:
                return 1.0
            half = fastPow(base, exp // 2)
            if exp % 2 == 0:
                return half * half
            else:
                return half * half * base

        if n < 0:
            return 1 / fastPow(x, -n)
        else:
            return fastPow(x, n)


            # it = 1
            # for i in range(0,n):
            #     it = it+it
            #     if(it<n):
            #         ans = ans*ans
            # return it

        # rem = n-0
        # ans = 1.00000
        # while(rem>0):
        #     rem = n - po(x,n)
        # return ans

        