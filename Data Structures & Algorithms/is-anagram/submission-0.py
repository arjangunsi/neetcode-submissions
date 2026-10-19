class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter not in d:
                d[letter] = 1
            else:
                d[letter] +=1
        for char in t:
            if char in d:
                d[char] -=1
            else:
                return False
        for x in d.values():
            if x != 0:        
                return False
        return True         
        
        