class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        if len(word1)<len(word2):
            short=word1
            long=word2
        else:
            short=word2
            long=word1     
        i=0
        while i<len(short):
            word=word+word1[i]+word2[i]
            i=i+1
        rest=long[i:]
        return word+rest