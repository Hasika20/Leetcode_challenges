class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=list(str(x))
        if x==x[::-1]:
            return True
        return False
        
        