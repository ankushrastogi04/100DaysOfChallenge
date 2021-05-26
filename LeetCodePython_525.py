# Given an integer number n, return the difference between the product of its digits and the sum of its digits.
# Example 1:
# Input: n = 234
# Output: 15 
# Explanation: 
# Product of digits = 2 * 3 * 4 = 24 
# Sum of digits = 2 + 3 + 4 = 9 
# Result = 24 - 9 = 15

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        mul=1
        su=0
        for i in n:
            mul=mul*int(i)
            su=su+int(i)
#print(mul)
        return(mul-su)




class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt=0
        while num>0:
            if num%2==0:
                cnt=cnt+1
                num=num/2-1
                cnt=cnt+1
    
        return(cnt)

#   1672. Richest Customer Wealth
# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.  
    class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        lar=0
        for i in accounts:
             if lar<sum(i):
                    lar=sum(i)
        return(lar)
