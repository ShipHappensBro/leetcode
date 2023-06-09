class Solution:
    def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        for elements in candies:
            kid=elements+extraCandies
            if kid>=max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
Solution.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3)