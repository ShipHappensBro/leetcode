class Solution:
    def gcdOfStrings( str1: str, str2: str) -> str:

        nod=iter=result=''
        
        for element in str1:
            iter+=element
            if iter in (str1 and str2):
                nod=iter
                
            if len(nod)>0:
                if (len(str1)/len(nod))==str1.count(nod) and (len(str2)/len(nod))==str2.count(nod):
                    result=nod

        return print(result)
    
Solution.gcdOfStrings(str1='ABABABAB',str2="ABAB")