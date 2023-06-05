class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=''
        for element in range(min(len(word1),len(word2))):
            result+=word1[element]+word2[element]
        return (result+word1[element+1:]+word2[element+1:])