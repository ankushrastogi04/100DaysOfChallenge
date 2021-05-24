# Given a string s, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.
# Example 1:
# Input: s = "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:
# Input: s = "aeiou"
# Output: ""

class Solution:
    def removeVowels(self, s: str) -> str:
        vow=['a', 'e', 'i', 'o', 'u']
        newLst=[]
        for ele in s:
            if ele not in vow:
                 newLst.append(ele)
        return(''.join(newLst) ) 

# Given a valid (IPv4) IP address, return a defanged version of that IP address.

# A defanged IP address replaces every period "." with "[.]".

# Example 1:

# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"
# Example 2:

# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"    
    
    class Solution:
    def defangIPaddr(self, address: str) -> str:
        newAdd=address.replace(".","[.]")   # string are immutable; we have store them into a new variable
        return newAdd
    
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
        
        
    class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        newList=[]
        sum=0
        for ele in nums:
            sum=sum+ele
            newList.append(sum)
            
        return   newList

#  Given the array candies and the integer extraCandies, where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies among the kids such that he or she can have the greatest number of candies among them. Notice that multiple kids can have the greatest number of candies.

# Example 1:

# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true] 
# Explanation: 
# Kid 1 has 2 candies and if he or she receives all extra candies (3) will have 5 candies --- the greatest number of candies among the kids. 
# Kid 2 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids. 
# Kid 3 has 5 candies and this is already the greatest number of candies among the kids. 
# Kid 4 has 1 candy and even if he or she receives all extra candies will only have 4 candies. 
# Kid 5 has 3 candies and if he or she receives at least 2 extra candies will have the greatest number of candies among the kids.    
    
    
  class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies=max(candies)
        newList=list()
        for i in candies:
            if extraCandies+i>=maxCandies:
                    newList.append(True)
            else:
                    newList.append(False)
        return newList            
          
    
    
#  Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].
# Example 1:

# Input: nums = [2,5,1,3,4,7], n = 3
# Output: [2,3,5,4,1,7] 
# Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].   
    
   class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        lst=[]
        for i in range(n):
            lst+=[nums[i]]
            lst+=[nums[i+n]]
        return(lst)  
         
    
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3    
    
    
    class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt=0
        for i in jewels:
            for j in stones:
                if i == j:
                    cnt=cnt+1
        return(cnt)            
     
        
        
# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

# Given the string command, return the Goal Parser's interpretation of command.

# Example 1:

# Input: command = "G()(al)"
# Output: "Goal"
# Explanation: The Goal Parser interprets the command as follows:
# G -> G
# () -> o
# (al) -> al
# The final concatenated result is "Goal".
    
    class Solution:
    def interpret(self, command: str) -> str:
        return(command.replace("()","o").replace("(al)","al"))
        #return(finalCommand)
