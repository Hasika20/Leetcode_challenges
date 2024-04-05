class Solution:
    def makeGood(self, s: str) -> str:
        while len(s) > 0:
            found_bad_pair = False
            for i in range(len(s) - 1):
                if (s[i].islower() and s[i+1] == s[i].upper()) or (s[i].isupper() and s[i+1] == s[i].lower()):
                    s = s[:i] + s[i+2:]
                    found_bad_pair = True
                    break  
            if not found_bad_pair:
                break 
        return s
