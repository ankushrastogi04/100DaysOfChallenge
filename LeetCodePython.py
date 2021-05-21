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
